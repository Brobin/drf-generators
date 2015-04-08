
from rest_framework.serializers import ModelSerializer
from api_v1.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content')

