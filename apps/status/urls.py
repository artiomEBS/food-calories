from django.urls import path

from apps.status.views import StatusView

urlpatterns = [
    path('today', StatusView.as_view(), name='status-today'),
]
