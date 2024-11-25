from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    profession_name = serializers.CharField(source="profession.name", read_only=True)
    state_name = serializers.CharField(source="state.name", read_only=True)
    city_name = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "name",
            "surname",
            "header",
            "profession",
            "profession_name",
            "state",
            "state_name",
            "city",
            "city_name",
            "about",
            "description",
            "phone",
            "certificate",
            "portfolio1",
            "portfolio2",
            "portfolio3",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "created_at", "updated_at"]

    def create(self, validated_data):
        user = validated_data.pop("user")  # Extrae el 'user' de validated_data
        return UserProfile.objects.create(user=user, **validated_data)
