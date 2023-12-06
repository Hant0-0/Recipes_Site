# Generated by Django 4.2.6 on 2023-12-03 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_project', '0008_alter_recipes_published_alter_recipes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='complexity',
            field=models.CharField(choices=[('Легко', 'Easy'), ('Середня', 'Aver'), ('Складно', 'Diff')], max_length=200, verbose_name='Складність'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 12, 58, 2, 95093, tzinfo=datetime.timezone.utc)),
        ),
    ]