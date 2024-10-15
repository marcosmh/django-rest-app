from rest_framework import serializers

from comments.models import Comment
from users.api.serializers import UserSerializer
from posts.api.serializer import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    class Meta:
         model = Comment
         fields = ['id','content','user','post','created_at']