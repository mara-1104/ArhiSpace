from django.urls import path
from .views import newsletter_view

urlpatterns = [

	path("", newsletter_view),
]
