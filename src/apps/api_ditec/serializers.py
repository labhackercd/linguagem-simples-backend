from rest_framework import serializers


class FileVideoSerializer(serializers.Serializer):
    url = serializers.CharField(required=True)
