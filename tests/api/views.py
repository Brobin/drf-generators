from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import CategorySerializer, PostSerializer
from api.models import Category, Post


class CategoryAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Category.objects.get(pk=id)
            serializer = CategorySerializer(item)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CategoryAPIListView(APIView):

    def get(self, request, format=None):
        items = Category.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PostAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Post.objects.get(pk=id)
            serializer = PostSerializer(item)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=404)
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PostAPIListView(APIView):

    def get(self, request, format=None):
        items = Post.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
