
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api_v1.serializers import PostSerializer
from api_v1.models import Post


class PostViewSet(ViewSet):

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=404)
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

