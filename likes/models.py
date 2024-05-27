from django.db import models
from django.contrib.auth import get_user_model
from comments.models import Comment

CustomUser = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
