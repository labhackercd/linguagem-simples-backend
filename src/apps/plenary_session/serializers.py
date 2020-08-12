from django.utils.translation import gettext_lazy as _
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

    def validate(self, data):
        try:
            if (bool(data['content']) is False and
                bool(data['tweet_url']) is False and
                    bool(data['image']) is False):
                raise serializers.ValidationError(
                    _('Content or tweet URL or image are required'))
        except KeyError as e:
            raise serializers.ValidationError(
                _('{} are required in json object'.format(e)))
        return data
