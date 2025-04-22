from django.shortcuts import render
from django.http import HttpResponse 
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

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Cat instances
cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})