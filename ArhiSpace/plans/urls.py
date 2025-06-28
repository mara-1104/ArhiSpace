from django.urls import path
from .views import plans_view

urlpatterns = [

	path("", plans_view),
]
