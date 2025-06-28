from django.urls import path
from .views import plans_view

urlpatterns = [

	path("planuri-si-preturi", plans_view),
]
