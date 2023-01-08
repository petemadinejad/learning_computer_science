from django.http import HttpResponse
from rest_framework import viewsets, serializers

from .models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class GetPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer