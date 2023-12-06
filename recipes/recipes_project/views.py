import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import authenticate
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .form import RecipeForm, MyUserCreationForm, CommentsForm
from .models import Recipes, Category, Comments
from .serializers import RecipeSerializer, CategoriesSerializer


# ---------- API --------#

class CategoriesAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True).data
        return Response(serializer)


class RecipesAPI(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipeSerializer(recipes, many=True).data
        return Response(serializer)
# ---------------------#


def home(request, category_slug=None):
    category = None

    categories = Category.objects.all()
    recipes = Recipes.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        recipes = Recipes.objects.filter(category=category)
    paginator = Paginator(recipes, 2)
    page_number = request.GET.get('page', 1)
    try:
        recipes_list = paginator.page(page_number)
    except PageNotAnInteger:
        recipes_list = paginator.page(1)
    except EmptyPage:
        recipes_list = paginator.page(paginator.num_pages)

    return render(request, 'recipes/home.html', {'category': category, 'categories': categories, 'recipes': recipes_list})


def register_user(request):
    if request.method == 'GET':
        return render(request, 'recipes/register_user.html', {'form': MyUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('current_recipes')
        else:
            return render(request, 'recipes/register_user.html',
                          {'form': MyUserCreationForm(), 'error': 'Password do not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'recipes/login_user.html', {'form': AuthenticationForm()})
    else:
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('current_recipes')
        except AttributeError:
            return render(request, 'recipes/login_user.html',
                          {'form': AuthenticationForm(), 'error': 'Passoword is not corrected'})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def current_recipes(request):
    recipes = Recipes.objects.filter(author=request.user)
    return render(request, 'recipes/current_recipes.html', {'recipes': recipes})


def create_recipes(request):
    if request.method == 'GET':
        return render(request, 'recipes/createrecipes.html', {'form': RecipeForm()})
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('current_recipes')


def change_recipes(request, rec_pk):
    recipes = get_object_or_404(Recipes, pk=rec_pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipes)
        return render(request, 'recipes/change_recipes.html', {'recipes': recipes, 'form': form})
    else:
        form = RecipeForm(request.POST, request.FILES, instance=recipes)
        form.save()
        return redirect('current_recipes')


def detail_recipe(request, year, month, day, recipe_slug):
    recipe = get_object_or_404(Recipes, slug=recipe_slug,
                               published__year=year,
                               published__month=month,
                               published__day=day)
    full_time = recipe.full_time
    ingredients = recipe.ingredients.split('\n')
    instructions_cooking = recipe.instructions_cooking.split('\n')

    comment_form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()

    return render(request, 'recipes/detail_recipe.html', {'recipe': recipe, 'full_time': full_time,
                                                          'ingredients': ingredients,
                                                          'instructions_cooking': instructions_cooking,
                                                          'comment_form': comment_form})


def delete_recipes(request, rec_pk):
    recipes = get_object_or_404(Recipes, pk=rec_pk, user=request.user)
    if request.method == 'POST':
        recipes.delete()
        return redirect('current_recipes')


def comments(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    comment = Comments.objects.filter(recipe=recipe_id)
    return render(request, 'recipes/comments.html', {'comments': comment, 'recipe': recipe})
