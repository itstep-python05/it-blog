from rest_framework import serializers
from ..models import BlogPost, BlogCategory


# Сериализатор категорий
class BlogCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogCategory
        fields = '__all__'


# Сериализатор постов
class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'


# Связующий сериализатор для добавления данных о категориях в пости
class BlogPostListRetrieveSerializer(serializers.ModelSerializer):

    blog_category = BlogCategorySerializer()

    class Meta:
        model = BlogPost
        fields = '__all__'


# Детализирующий сериализатор для вывода списка постов данной категории
class BlogCategoryDetailSerializer(serializers.ModelSerializer):

    posts = serializers.SerializerMethodField()

    class Meta:
        model = BlogCategory
        fields = '__all__'

    @staticmethod
    def get_posts(obj):
        return BlogPostSerializer(BlogPost.objects.filter(blog_category=obj), many=True).data
