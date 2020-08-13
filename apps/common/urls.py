from django.urls import re_path
from apps.common import views

urlpatterns = [
    re_path(r'test/route/', views.TestView.as_view(), name='test_view'),
]
