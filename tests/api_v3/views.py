
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_v3.models import Post
from api_v3.serializers import PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        items = Post.objects.all()
        serializer = PostSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        item = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = PostSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
