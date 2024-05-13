from rest_framework import generics

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        ).order_by('-created_at')


class NotificationUpdateView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
