from django.apps import AppConfig

# ---------------------------------------
# App Configuration for 'main_app'
# ---------------------------------------


class MainAppConfig(AppConfig):
    # This class defines settings and metadata for the 'main_app' Django application.

    default_auto_field = "django.db.models.BigAutoField"
    # Sets the default field type for auto-generated primary keys.
    # "BigAutoField" is used instead of "AutoField" for scalability (handles big IDs).

    name = "main_app"
    # This must match the folder name of your app (in this case, 'main_app').
    # Django uses this to locate app components like models, views, templates, etc.
