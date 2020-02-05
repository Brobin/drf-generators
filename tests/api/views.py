from rest_framework.viewsets import ModelViewSet
from api.serializers import CategorySerializer, PostSerializer
from api.models import Category, Post


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.order_by('pk')
    serializer_class = PostSerializer
