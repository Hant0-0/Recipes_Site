from django.urls import path
from recipes_project import views

urlpatterns = [
    path('', views.home, name='home'),
    path('current/', views.current_recipes, name='current_recipes'),
    path('create/', views.create_recipes, name="createrecipes"),
    path('change_recipes/<int:rec_pk>', views.change_recipes, name="change_recipes"),
    path('<int:year>/<int:month>/<int:day>/<slug:recipe_slug>', views.detail_recipe, name="detail_recipe"),
    path('delete/<int:rec_pk>', views.delete_recipes, name="deleterecipes"),
    path('<slug:category_slug>/', views.home, name='home'),

    path('comments/<int:recipe_id>', views.comments, name='comments'),

    ##Filter
    path('<slug:country_slug>/', views.home, name='home'),
]