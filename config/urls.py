from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


openapi_info = openapi.Info(
    title="Food Calorie API Documentation",
    default_version='v1',
    description="Food Calorie API documentation",
)

schema_view = get_schema_view(
    openapi_info,
    validators=['ssv'],
    public=True,
    permission_classes=(AllowAny,)
)

swagger_view = schema_view.with_ui('swagger', cache_timeout=0)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.calorie_api.urls'), name='api'),
    path('track/', include('apps.journal.urls'), name='journal'),
    path('search/', include('apps.search.urls'), name='search'),
    path('status/', include('apps.status.urls'), name='user'),
    path('diary/', include('apps.diary.urls'), name='diary'),
    path('foodstuff/', include('apps.foodstuff.urls'), name='foodstuff'),
    path('user/', include('apps.users.urls'), name='user'),
    path('', swagger_view, name='schema-swagger-ui'),
]
