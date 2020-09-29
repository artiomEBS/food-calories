from rest_framework.routers import DefaultRouter
from apps.calorie_api import views


router = DefaultRouter()

router.register('food/category', views.FoodCategoryViewSet, basename='food-category')
router.register('food/portion', views.FoodPortionViewSet, basename='food-portion')
router.register('food', views.FoodViewSet, basename='food')
router.register('activity', views.ActivityViewSet, basename='activity')

urlpatterns = router.urls