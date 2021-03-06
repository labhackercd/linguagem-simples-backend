from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import PlenarySession, Publication, SavedContent
from apps.authentication.serializers import UserSerializer


class PlenarySessionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = PlenarySession
        exclude = ['modified', 'created']

    def validate(self, data):
        if not self.instance:
            if not data['enable'] and data['resume']:
                raise serializers.ValidationError(
                    _('Only session enable can have resume'))
        return data


class PublicationSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Publication
        exclude = ['modified']

    def validate(self, data):
        if not self.instance:
            try:
                if (bool(data['content']) is False and
                    bool(data['tweet_id']) is False and
                        bool(data['image']) is False):
                    raise serializers.ValidationError(
                        _('Content or tweet_id or image are required'))
            except KeyError as e:
                raise serializers.ValidationError(
                    _('{} are required in json object'.format(e)))
            session = data['session']
            if not session.enable:
                raise serializers.ValidationError(
                    _('Only session enable can have publication'))
        return data


class SavedContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedContent
        exclude = ['modified']
