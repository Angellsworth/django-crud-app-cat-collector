from django.urls import path
from . import views  # Imports all view functions and class-based views from views.py

urlpatterns = [
    # Home page route (LoginView-based, displays login form)
    path("", views.Home.as_view(), name="home"),

    # About page route (static info, function-based view)
    path("about/", views.about, name="about"),

    # Route to display all cats belonging to the logged-in user
    path("cats/", views.cat_index, name="cat-index"),

    # Route to display details for a single cat by its ID
    path("cats/<int:cat_id>/", views.cat_detail, name="cat-detail"),

    # Route to show a form for creating a new cat
    # Uses CreateView with form_valid method assigning the logged-in user
    path("cats/create/", views.CatCreate.as_view(), name="cat-create"),

    # Route to show a form for editing an existing cat (identified by primary key)
    path("cats/<int:pk>/update/", views.CatUpdate.as_view(), name="cat-update"),

    # Route to confirm and delete a cat (uses DeleteView)
    path("cats/<int:pk>/delete/", views.CatDelete.as_view(), name="cat-delete"),

    # Route to add a feeding record to a specific cat (handled via POST on cat detail page)
    path("cats/<int:cat_id>/add-feeding/", views.add_feeding, name="add-feeding"),

    # Route to show a form for creating a new toy
    path("toys/create", views.ToyCreate.as_view(), name="toy-create"),

    # Route to view details of a specific toy
    path("toys/<int:pk>/", views.ToyDetail.as_view(), name="toy-detail"),

    # Route to view a list of all toys
    path("toys/", views.ToyList.as_view(), name="toy-index"),

    # Route to show a form for editing a toy
    path("toys/<int:pk>/update/", views.ToyUpdate.as_view(), name="toy-update"),

    # Route to confirm and delete a toy
    path("toys/<int:pk>/delete/", views.ToyDelete.as_view(), name="toy-delete"),

    # Route to associate a toy with a cat (many-to-many relationship)
    # Called from a form on the cat detail page
    path('cats/<int:cat_id>associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),

    # Route to remove the toy-to-cat association
    path('cats/<int:cat_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),

    path('accounts/signup/', views.signup, name='signup'),
]