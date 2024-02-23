import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from googletrans import Translator


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    image = models.ImageField(upload_to='category', default='')
    slug = models.SlugField(db_index=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        translater = Translator()
        translation = translater.translate(str(self.name), 'en')
        self.slug = slugify(translation.text, 'en')
        super(Category, self).save(*args, **kwargs)


class Recipes(models.Model):
    comp = [
        ('Легко', 'Легко'),
        ('Середня', 'Середня'),
        ('Складно', 'Складно'),
    ]

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=120, unique_for_date='published')
    description = models.TextField(blank=True, verbose_name='Опис')
    ingredients = models.TextField(blank=True, verbose_name="Інгредієнти")
    instructions_cooking = models.TextField(blank=True, verbose_name='Інструкція приготування')
    complexity = models.CharField(max_length=200, choices=comp, verbose_name="Складність")
    preparation_time = models.TimeField(blank=True, verbose_name="Час підготовки")
    cooking_time = models.TimeField(blank=True, verbose_name="Час приготування")
    image = models.ImageField(upload_to='images', verbose_name="Фото страви")
    published = models.DateTimeField(default=timezone.now())
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата і час створення")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата і час оновлення")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    category = models.ForeignKey(Category, models.CASCADE, verbose_name="Категорія")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепти"
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
        ]

    def __str__(self):
        return self.title

    @property
    def full_time(self):
        one_time = (int(self.preparation_time.hour) * 3600 +
                    int(self.preparation_time.minute) * 60 +
                    int(self.preparation_time.second))

        two_time = (int(self.cooking_time.hour) * 3600 +
                    int(self.cooking_time.minute) * 60 +
                    int(self.cooking_time.second))
        sum_time = one_time + two_time
        full = datetime.time(sum_time // 3600, (sum_time % 3600) // 60, sum_time % 60)
        return full

    def get_absolute_url(self):
        return reverse('recipes:detail_recipe', args=[self.published.year,
                                                      self.published.month,
                                                      self.published.day,
                                                      self.slug])

    def save(self, *args, **kwargs):
        translater = Translator()
        translation = translater.translate(str(self.title), 'en')
        self.slug = slugify(translation.text, 'en')
        super(Recipes, self).save(*args, **kwargs)


class Comments(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=120, verbose_name='Ім`я')
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Коментар')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.name} in {self.recipe}'
