from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from recipes_project import views
from recipes_project.views import RecipesAPI, RecipesAPIDetail

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('login/', views.register_user, name='register_user'),
    path('signin/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logoutuser'),

    #Recipes
    path('', include(('recipes_project.urls', 'recipes_project'), namespace='recipes')),

    #API
    path('api/v1/categories/',  views.CategoriesAPI.as_view()),
    path('api/v1/categori/<int:cat_id>/',  views.CategoriDetailAPI.as_view()),
    path('api/v1/recipes', RecipesAPI.as_view()),
    path('api/v1/recipe/<int:recipe_id>/', RecipesAPIDetail.as_view()),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)