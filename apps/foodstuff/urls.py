from django.urls import path
from apps.foodstuff import views

urlpatterns = [
    path('food/<int:pk>/', views.FoodStuffFoodDetailView.as_view(), name='foodstuff-food-detail'),
    path('food/portion/<int:pk>/',views.FoodStuffFoodPortionDetailView.as_view(), name='foodstuff-food-portion-detail'),
    path('food/category/<int:pk>/', views.FoodStuffFoodCategoryDetailView.as_view(), name='foodstuff-food-detail'),
    path('activity/<int:pk>/', views.FoodStuffActivityDetailView.as_view(), name='foodstuff-activity-detail'),
    path('activity', views.FoodStuffActivityCreateView.as_view(), name='foodstuff-activity'),
    path('food', views.FoodStuffFoodCreateView.as_view(), name='foodstuff-food'),
    path('food/category', views.FoodStuffFoodCategoryCreateView.as_view(), name='foodstuff-food-category-create'),
    path('food/portion', views.FoodStuffFoodPortionCreateView.as_view(), name='foodstuff-food-portion-create'),




]
