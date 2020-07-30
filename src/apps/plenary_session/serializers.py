from rest_framework import serializers
from .models import PlenarySession, Publication
from apps.authentication.serializers import UserSerializer


class PlenarySessionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = PlenarySession
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'
