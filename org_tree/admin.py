from django.contrib import admin
from django.apps import apps

# Get the app configuration for 'org_tree'
app = apps.get_app_config('org_tree')

# Register all models in 'org_tree' with the admin site
for model_name, model in app.models.items():
    # Define a new admin class for each model
    class ModelAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields if field.name != "id"]
        search_fields = [field.attname for field in model._meta.fields]
        show_full_result_count = True

    # Register the model with the admin site using the dynamically created admin class
    admin.site.register(model, ModelAdmin)
