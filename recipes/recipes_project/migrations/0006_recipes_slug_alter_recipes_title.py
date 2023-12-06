# Generated by Django 4.2.6 on 2023-11-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_project', '0005_alter_recipes_options_alter_recipes_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='slug',
            field=models.CharField(db_index=True, default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
    ]
