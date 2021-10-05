from django.urls import path

from api import views

# Create a router and register our viewsets with it.


# The API URLs are now determined automatically by the router.

# urlpatterns = [    path('v1', include(router.urls)),]

from django.views.generic import TemplateView

urlpatterns = [
    # ... previously defined routes
    path("home", views.home),
    path("home1", views.home1),
    path("home2", views.home2),
    path("home3", views.home3),



]


