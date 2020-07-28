from rest_framework import serializers
from .models import PlenarySession


class PlenarySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlenarySession
        fields = '__all__'
