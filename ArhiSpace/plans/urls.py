from django.urls import path
from .views import estimare_view

urlpatterns = [

	path("", estimare_view),

]

