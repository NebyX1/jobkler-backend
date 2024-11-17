from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        if profile_id:
            return Review.objects.filter(profile_id=profile_id)
        return Review.objects.all()


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        profile_id = self.request.data.get("profile")

        # Verificar si el usuario ya ha escrito una reseña para el perfil
        if Review.objects.filter(user=user, profile_id=profile_id).exists():
            raise ValidationError(
                {
                    "code": "review_exists",
                    "message": "Ya has escrito una reseña para este perfil."
                },
                code=status.HTTP_400_BAD_REQUEST
            )

        try:
            serializer.save(user=user)
        except Exception:
            raise ValidationError(
                {
                    "code": "creation_failed",
                    "message": "No se pudo crear la reseña. Intenta nuevamente más tarde."
                },
                code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        review = super().get_object()
        if review.user != self.request.user:
            raise PermissionDenied(
                {
                    "code": "permission_denied",
                    "message": "No tienes permiso para eliminar esta reseña."
                }
            )
        return review

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception:
            raise ValidationError(
                {
                    "code": "deletion_failed",
                    "message": "No se pudo eliminar la reseña. Intenta nuevamente más tarde."
                },
                code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
