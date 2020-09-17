from django.urls import path
from apps.diary import views


urlpatterns = [
    path('food/', views.DiaryFoodView.as_view(), name='diary-food'),
    path('activity/', views.DiaryActivityView.as_view(), name='diary-activity'),
]
