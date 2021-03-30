from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import (
    BlogCategorySerializer,
    BlogPostSerializer,
    BlogPostListRetrieveSerializer,
    BlogCategoryDetailSerializer
)
from ..models import BlogCategory, BlogPost


# Набор предаставлений категорий
class BlogCategoryViewSet(viewsets.ModelViewSet):

    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

    action_to_serializer = {
        "retrieve": BlogCategoryDetailSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(self.action, self.serializer_class)


# Набор предаставлений постов
class BlogPostViewSet(viewsets.ModelViewSet):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    action_to_serializer = {
        "list": BlogPostListRetrieveSerializer,
        "retrieve": BlogPostListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(self.action, self.serializer_class)


class TestAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        users = [
            {"id": 1, "first_name": "Jhon", "last_name": "Wick", "age": 41},
            {"id": 2, "first_name": "Elon", "last_name": "Mask", "age": 47},
            {"id": 3, "first_name": "Nikola", "last_name": "Tesla", "age": 45}
        ]
        return Response(users)
