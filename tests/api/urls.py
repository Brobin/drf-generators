from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'category', views.CategoryViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = router.urls
