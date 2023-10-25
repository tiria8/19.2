from datetime import date

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    product_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(default=date.today, verbose_name='дата создания')
    last_edited = models.DateField(default=date.today, verbose_name='дата последнего изменения')

    def __str__(self):
        return self.name

    @property
    def active_version(self):
        return Version.objects.filter(is_active=True, product=self.id).first()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug')
    description = models.TextField(verbose_name='Содержание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(default=date.today, verbose_name='дата создания')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    is_viewable = models.BooleanField(default=True, verbose_name='признак публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(default=1, verbose_name='номер версии')
    version_title = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return self.version_title

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
