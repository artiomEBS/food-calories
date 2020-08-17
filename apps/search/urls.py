from rest_framework.routers import DefaultRouter
from apps.search import views


router = DefaultRouter()

router.register('food-category', views.SearchFoodCategoryViewSet, basename='food-category')
router.register('food-portion', views.SearchFoodPortionViewSet, basename='food-portion')
router.register('food-journal', views.SearchFoodJournalViewSet, basename='journal')
router.register('food', views.SearchFoodViewSet, basename='food')
router.register('activity-journal', views.SearchActivityJournalViewSet, basename='journal')
router.register('activity', views.SearchActivityViewSet, basename='activity')

urlpatterns = router.urls
