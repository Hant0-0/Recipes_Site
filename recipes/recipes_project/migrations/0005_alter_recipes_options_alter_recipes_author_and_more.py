# Generated by Django 4.2.6 on 2023-11-30 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes_project', '0004_alter_category_options_alter_recipes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipes',
            options={'ordering': ['-create_at'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепти'},
        ),
        migrations.AlterField(
            model_name='recipes',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='recipes',
            index=models.Index(fields=['-create_at'], name='recipes_pro_create__953b94_idx'),
        ),
    ]
