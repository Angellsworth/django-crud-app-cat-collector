from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, FeedingForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cat, Toy

# ---------- AUTH VIEW ----------

# Uses Django's built-in LoginView to render and handle the login page
class Home(LoginView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('cat-index')
        return super().dispatch(request, *args, **kwargs)

# ---------- STATIC & SIMPLE ROUTES ----------

def about(request):
    # Renders the About page with contact information.
    return render(request, "about.html", {
        "contact": "You can reach support at support@catcollector.com"
    })

# ---------- CAT VIEWS ----------

@login_required
def cat_index(request):
    # Filters cats by currently logged-in user
    cats = Cat.objects.filter(user=request.user)
    return render(request, "cats/index.html", {"cats": cats})

def cat_detail(request, cat_id):
    # Displays one cat and its toys/feedings
    cat = Cat.objects.get(id=cat_id)
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have
    })

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ["name", "breed", "description", "age"]

    def form_valid(self, form):
        # Link new cat to logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = ["breed", "description", "age"]

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = "/cats/"

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect("cat-detail", cat_id=cat_id)

# ---------- TOY VIEWS ----------

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = "__all__"

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ["name", "color"]

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = "/toys/"

# ---------- CAT <--> TOY RELATIONSHIP VIEWS ----------

def associate_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
    cat = Cat.objects.get(id=cat_id)
    cat.toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat.id)

# ---------- SIGNUP VIEW ----------

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login new user
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
