# Generated by Django 4.2.6 on 2023-11-29 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_project', '0003_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='recipes',
            options={'ordering': ['id'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепти'},
        ),
    ]
