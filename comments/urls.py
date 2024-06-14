from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_comment),
    path('<int:comment_id>/likes', views.add_like_to_comment, name='add_like_to_comment'),
]
