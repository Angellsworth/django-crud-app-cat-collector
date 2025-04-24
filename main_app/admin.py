from django.contrib import admin
from .models import Cat, Feeding, Toy

# ---------------------------------------
# Django Admin Configuration
# ---------------------------------------

# Register each model so it shows up in the Django admin dashboard.
# This allows you to add, edit, and delete these models via the built-in admin UI.

admin.site.register([Cat, Feeding, Toy])
# Now you can manage Cat entries from the admin panel
# Lets you view, add, and remove feeding records in the admin
# Lets you manage all available toys directly from the admin