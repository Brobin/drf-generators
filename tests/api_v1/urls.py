
from rest_framework.routers import SimpleRouter
from api_v1 import views


router = SimpleRouter()

router.register(r'post', views.PostViewSet, 'Post')

urlpatterns = router.urls
