from django.urls import path
from .views import team_view

urlpatterns = [

	path("echipa-noastra", team_view),
]
