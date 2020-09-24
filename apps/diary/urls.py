from django.urls import path
from apps.diary import views


urlpatterns = [
    path('status/', views.DiaryStatusDetailView.as_view(), name='daily-status'),
    path('food/', views.DiaryFoodCreateView.as_view(), name='diary-food-create'),
    path('food/<int:pk>/', views.DiaryFoodDetailView.as_view(), name="diary-food-detail"),
    path('activity/', views.DiaryActivityCreateView.as_view(), name='diary-activity-create'),
    path('activity/<int:pk>/', views.DiaryActivityDetailView.as_view(), name='diary-activity-detail'),
]
