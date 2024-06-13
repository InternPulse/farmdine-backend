from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('comments.Comment', related_name='comment_likes', on_delete=models.CASCADE)

