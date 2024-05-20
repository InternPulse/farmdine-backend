from django.db import models

class Event(models.Model):
    """Model representing an event."""
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """String representation of the event."""
        return self.title

class Comment(models.Model):
    """Model representing a comment."""
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        """String representation of the comment."""
        return self.text

class Like(models.Model):
    """Model representing a like."""
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)

