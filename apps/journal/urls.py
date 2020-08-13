from rest_framework.routers import DefaultRouter
from apps.journal import views


router = DefaultRouter()

router.register('food-portion', views.FoodPortionViewSet, basename='food-portion')
router.register('food-category', views.FoodCategoryViewSet, basename='food-category')
router.register('food-journal', views.FoodJournalViewSet, basename='food-journal')
router.register('food', views.FoodViewSet, basename='food')
router.register('activity-category', views.ActivityCategoryViewSet, basename='activity-category')
router.register('activity-journal', views.ActivityJournalViewSet, basename='activity-journal')
router.register('activity', views.ActivityViewSet, basename='activity')

urlpatterns = router.urls
