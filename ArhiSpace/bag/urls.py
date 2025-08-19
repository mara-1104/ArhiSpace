from django.urls import path
from .views import bag_view

urlpatterns = [

	path("", bag_view, name="bag"),
]
