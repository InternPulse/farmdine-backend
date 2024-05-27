from django.urls import path
from . import views

urlpatterns = [
    path('api/likes/', views.add_like),
]
