from rest_framework.serializers import ModelSerializer
from api.models import Category, Post


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
