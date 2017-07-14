from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from post.models import LostPost
from post.permissions import IsOwnerOrReadOnly
from post.serializer import LostSerializer


class LostViewSet(viewsets.ModelViewSet):
    queryset = LostPost.objects.all()
    serializer_class = LostSerializer

    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
