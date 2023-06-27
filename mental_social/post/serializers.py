from rest_framework import serializers
from .models import Post, Comment

# class NestedCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'content', 'author', 'created_at', 'updated_at' , 'parent')


class CommentSerializer(serializers.ModelSerializer):
    # replies = NestedCommentSerializer(many=True, required=False ,read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'author', 'created_at', 'updated_at')
        read_only_fields = ['author', 'created_at', 'updated_at']


