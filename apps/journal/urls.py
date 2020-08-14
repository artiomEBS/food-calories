from rest_framework.routers import DefaultRouter
from apps.journal import views


router = DefaultRouter()

router.register('food', views.FoodJournalViewSet, basename='food-journal')
router.register('activity', views.ActivityJournalViewSet, basename='activity-journal')

urlpatterns = router.urls
