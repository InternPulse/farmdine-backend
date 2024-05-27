from django.urls import path
from . import views

urlpatterns = [
    path('api/comments/', views.add_comment),
    path('api/comments/<int:comment_id>/likes/', views.add_like_to_comment),
]
