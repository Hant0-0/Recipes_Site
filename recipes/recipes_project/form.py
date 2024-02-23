from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import QueryDict
from django.utils.text import slugify

from .models import Recipes, Comments


class RecipeForm(ModelForm):

    class Meta:
        model = Recipes
        fields = ['title', 'description', 'ingredients', 'instructions_cooking', 'complexity', 'preparation_time',
                  'cooking_time', 'image', 'author', 'category']


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {'password1': '', 'password2': '', 'username': ''}


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body', 'name', 'email']