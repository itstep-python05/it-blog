from django.db import models


# Модель категории статьи
class BlogCategory(models.Model):

    name = models.CharField(max_length=256, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


# Менеджер модели постов
class BlogPostManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def all(self):
        return self.get_queryset().filter(in_archive=False)


# Модель поста
class BlogPost(models.Model):

    blog_category = models.ForeignKey(BlogCategory, verbose_name="Имя категории", on_delete=models.CASCADE)
    title = models.CharField(max_length=256, verbose_name="Заголовок статьи")
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=1024, verbose_name="Содержание статьи")
    image = models.FileField(upload_to='blog_posts/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    in_archive = models.BooleanField(default=False, verbose_name="В архиве")
    objects = BlogPostManager()

    def __str__(self) -> str:
        return f'{self.title} из категории: "{self.blog_category.name}"'
