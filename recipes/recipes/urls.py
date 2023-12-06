from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from recipes_project import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('login/', views.register_user, name='register_user'),
    path('signin/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logoutuser'),

    #Recipes
    path('', include(('recipes_project.urls', 'recipes_project'), namespace='recipes')),

    #API
    path('api/categories/',  views.CategoriesAPI.as_view()),
    path('api/recipes/',  views.RecipesAPI.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)