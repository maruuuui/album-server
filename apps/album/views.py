from rest_framework import viewsets
from django.middleware.csrf import get_token
from .models import Image
from .serializers import ImageSerializer
from django.http.response import JsonResponse


class ImageViewSet(viewsets.ModelViewSet):
    """
        画像と画像の推論結果の詳細
    """

    queryset = Image.objects.all().order_by("-created_at")
    serializer_class = ImageSerializer


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({"token": token})
