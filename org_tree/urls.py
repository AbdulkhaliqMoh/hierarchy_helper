from django.urls import path
from . import views

# Define the namespace for this Django app. 
# This is useful for reversing URLs to this app's views.
app_name = 'org_tree'

# URL patterns for the org_tree app.
urlpatterns = [
    # When the user visits the root URL of the org_tree app (e.g., /org_tree/),
    path('', views.units_list, name='index')
]
