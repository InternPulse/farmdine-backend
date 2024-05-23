from rest_framework import generics
from .models import Comment, Like, Event
from .serializers import CommentSerializer, LikeSerializer, EventSerializer


class EventListCreate(generics.ListCreateAPIView):
    """ API endpoint for listing and creating events."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a specific event."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CommentCreate(generics.CreateAPIView):
    """API endpoint for creating a comment related to a specific event."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Perform creation of the comment related to a specific event."""
        event_id = self.kwargs['event_id']
        event = Event.objects.get(id=event_id)
        serializer.save(event=event)


class LikeCreate(generics.CreateAPIView):
    """API endpoint for creating a like for a comment."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDelete(generics.DestroyAPIView):
    """API endpoint for deleting a like."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_url_kwarg = 'like_id'
