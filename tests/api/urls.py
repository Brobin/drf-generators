from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'post', views.PostViewSet, 'Post')

urlpatterns = router.urls
