from django.urls import path
from .views import TestAPIView
from rest_framework import routers
from .views import BlogCategoryViewSet, BlogPostViewSet

router = routers.SimpleRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('blogpost', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('test-api/', TestAPIView.as_view(), name='test')
]

urlpatterns += router.urls
