from rest_framework import serializers
from .models import Review
from apps.user_profile.models import UserProfile  # Importamos UserProfile


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    profile = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'profile', 'stars', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        if data['profile'].user == self.context['request'].user:
            raise serializers.ValidationError("No puedes dejar una reseña sobre tu propio perfil.")
        return data
