from django.urls import path
from apps.status.views import StatusView


urlpatterns = [
    path('daily/', StatusView.as_view(), name='daily-status')
]
