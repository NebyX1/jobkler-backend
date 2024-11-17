from rest_framework import serializers
from .models import Favourite
from apps.user_profile.models import UserProfile


class FavouriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    profile = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    profile_user_id = serializers.IntegerField(read_only=True)  # Eliminado source='profile_user_id'

    class Meta:
        model = Favourite
        fields = ['id', 'user', 'profile', 'profile_user_id', 'created_at']  # Incluye profile_user_id
        read_only_fields = ['id', 'created_at', 'profile_user_id']

    def create(self, validated_data):
        user = self.context['request'].user
        profile = validated_data['profile']
        favourite, created = Favourite.objects.get_or_create(user=user, profile=profile)
        return favourite
