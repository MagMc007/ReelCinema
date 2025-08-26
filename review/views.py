from rest_framework import permissions 
from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ ensures only the owner can edit/delete """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class ReviewView(ModelViewSet):
    """ view set for reviews """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ["movie"]
    pagination_class = [PageNumberPagination]
    ordering = ["-created_at"]
    
    def perform_create(self, serializer):
        # save the current review to the current user
        serializer.save(user=self.request.user)
