
from rest_framework.serializers import ModelSerializer
from api_v3.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post

