from rest_framework import serializers
from .models import Location, Profession


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'code']
        extra_kwargs = {
            'code': {
                'required': False,
                'allow_blank': True,
                'allow_null': True,
                'read_only': False  # Permite que se pueda asignar manualmente
            }
        }


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'name', 'code']
        extra_kwargs = {
            'code': {
                'required': False,
                'allow_blank': True,
                'allow_null': True,
                'read_only': False  # Permite que se pueda asignar manualmente
            }
        }
