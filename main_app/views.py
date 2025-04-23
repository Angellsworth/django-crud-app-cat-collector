from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat

# Create your views here.

#controller code in python
#we call these view functions
def home(request):
    #each view function or "view"
    #recieves a request object
    return render(request, 'home.html')
#to send a response, we return it

def about(request):
    contact_details = 'You can reach support at support@catcollector.com'
    return render(request, 'about.html', {
        'contact': contact_details
    })

# views.py

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request,'cats/detail.html', {
        'cat': cat
    })

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/cats' #takes us to index. Not preferred way.
   