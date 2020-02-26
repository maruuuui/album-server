from rest_framework import serializers

from apps.album.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_name = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ("id", "image_name", "image", "memo", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    def get_image_name(self, obj):
        return obj.image.name
