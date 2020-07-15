from django.contrib.auth import get_user_model

from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

router = DefaultRouter()
router.register("users", UsersViewSet)

# User = get_user_model()

urlpatterns = router.urls