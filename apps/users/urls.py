from django.urls import path
from apps.users import views

urlpatterns = [
    path('apikey/', views.GenerateApikey.as_view(), name='get_apikey'),
    path('apikey/profile/', views.ProfileListView.as_view(), name='get_profile')
]
