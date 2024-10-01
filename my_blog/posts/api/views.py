from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostApiView(APIView):
    def get(self, request):
        #posts = Post.objects.all()
        # posts = [post.title for post in Post.objects.all()]
        # return Response(status=status.HTTP_200_OK,data=posts)
        serializer = PostSerializer(Post.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    
    def post(self, request):
        #Post.objects.create(title=request.POST['title'], 
        #                    description=request.POST['description'], 
        #                    order=request.POST['order'])
        #  return self.get(request)
        serializer = PostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
      