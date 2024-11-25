from rest_framework import serializers
from .models import State, City, Profession


# Serializador para los estados
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'code']
        extra_kwargs = {
            'code': {
                'required': False,
                'allow_blank': True,
                'allow_null': True,
                'read_only': False
            }
        }


# Serializador para las ciudades
class CitySerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(
        slug_field='name',
        queryset=State.objects.all()
    )

    class Meta:
        model = City
        fields = ['id', 'name', 'code', 'state']
        extra_kwargs = {
            'code': {
                'required': False,
                'allow_blank': True,
                'allow_null': True,
                'read_only': False
            }
        }


# Serializador para las profesiones
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'name', 'code']
        extra_kwargs = {
            'code': {
                'required': False,
                'allow_blank': True,
                'allow_null': True,
                'read_only': False
            }
        }
