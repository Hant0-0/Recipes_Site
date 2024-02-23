import datetime
from rest_framework import serializers
from recipes_project.models import Recipes, Category


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    total_time = serializers.SerializerMethodField()

    def get_total_time(self, instance):
        one_time = (int(instance.preparation_time.hour) * 3600 +
                    int(instance.preparation_time.minute) * 60
                    + int(instance.preparation_time.second))
        two_time = (int(instance.cooking_time.hour) * 3600 +
                    int(instance.cooking_time.minute) * 60
                    + int(instance.cooking_time.second))
        sum_time = one_time + two_time
        full_time = datetime.time(sum_time//3600, (sum_time%3600)//60, sum_time%60)
        return full_time


    class Meta:
        model = Recipes
        fields = ['title', 'description', 'ingredients', 'instructions_cooking', 'complexity',
                  'preparation_time', 'cooking_time', 'total_time', 'image', 'create_at', 'update_at', 'author',
                  'category']



