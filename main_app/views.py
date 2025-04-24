from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from .models import Cat, Toy

# ---------- STATIC & SIMPLE ROUTES ----------

def home(request):
    # Renders the home (login) page.
    # URL: path("", views.home, name="home")
    # Template: templates/home.html
    return render(request, "home.html")

def about(request):
    # Renders the About page.
    # URL: path("about/", views.about, name="about")
    # Template: templates/about.html
    return render(request, "about.html", {"contact": "You can reach support at support@catcollector.com"})


# ---------- CAT VIEWS ----------

def cat_index(request):
    # Shows a list of all cats.
    # (In production, you'll likely filter by user: Cat.objects.filter(user=request.user))
    # URL: path("cats/", views.cat_index, name="cat-index")
    # Template: templates/cats/index.html
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {"cats": cats})


def cat_detail(request, cat_id):
    # Displays the detail page for one cat, including feedings and toys.
    # URL: path("cats/<int:cat_id>/", views.cat_detail, name="cat-detail")
    # Template: templates/cats/detail.html

    cat = Cat.objects.get(id=cat_id)

    # Exclude toys the cat already has from the list of available toys
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))

    feeding_form = FeedingForm()

    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have  # these are the toys we can still give the cat
    })


class CatCreate(CreateView):
    # View to create a new cat.
    # URL: path("cats/create/", views.CatCreate.as_view(), name="cat-create")
    # Template: templates/cats/cat_form.html
    model = Cat
    fields = ["name", "breed", "description", "age"]


class CatUpdate(UpdateView):
    # View to update a cat's breed, description, and age (not name).
    # URL: path("cats/<int:pk>/update/", views.CatUpdate.as_view(), name="cat-update")
    # Template: templates/cats/cat_form.html
    model = Cat
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    # View to delete a cat.
    # URL: path("cats/<int:pk>/delete/", views.CatDelete.as_view(), name="cat-delete")
    # Template: templates/cats/cat_confirm_delete.html
    model = Cat
    success_url = "/cats/"  # Redirect after successful delete


def add_feeding(request, cat_id):
    # Handles POST form submission to add a feeding to a cat.
    # URL: path("cats/<int:cat_id>/add-feeding/", views.add_feeding, name="add-feeding")
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect("cat-detail", cat_id=cat_id)


# ---------- TOY VIEWS ----------

class ToyCreate(CreateView):
    # View to create a new toy.
    # URL: path("toys/create", views.ToyCreate.as_view(), name="toy-create")
    # Template: templates/toys/toy_form.html
    model = Toy
    fields = "__all__"


class ToyList(ListView):
    # View to list all toys.
    # URL: path("toys/", views.ToyList.as_view(), name="toy-index")
    # Template: templates/toys/toy_list.html
    model = Toy


class ToyDetail(DetailView):
    # View to show one toy's details.
    # URL: path("toys/<int:pk>/", views.ToyDetail.as_view(), name="toy-detail")
    # Template: templates/toys/toy_detail.html
    model = Toy


class ToyUpdate(UpdateView):
    # View to update a toy's name or color.
    # URL: path("toys/<int:pk>/update/", views.ToyUpdate.as_view(), name="toy-update")
    # Template: templates/toys/toy_form.html
    model = Toy
    fields = ["name", "color"]


class ToyDelete(DeleteView):
    # View to delete a toy.
    # URL: path("toys/<int:pk>/delete/", views.ToyDelete.as_view(), name="toy-delete")
    # Template: templates/toys/toy_confirm_delete.html
    model = Toy
    success_url = "/toys/"


# ---------- CAT <--> TOY RELATIONSHIP VIEWS ----------

def associate_toy(request, cat_id, toy_id):
    # Associates a toy with a cat (adds to the many-to-many field).
    # URL: path("cats/<int:cat_id>associate-toy/<int:toy_id>/", views.associate_toy, name="associate-toy")
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)


def remove_toy(request, cat_id, toy_id):
    # Removes a toy from a cat's toy list (removes from many-to-many field).
    # URL: path("cats/<int:cat_id>/remove-toy/<int:toy_id>/", views.remove_toy, name="remove-toy")
    cat = Cat.objects.get(id=cat_id)
    cat.toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat.id)