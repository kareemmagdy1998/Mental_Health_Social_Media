from .models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    # replies = NestedCommentSerializer(many=True, required=False ,read_only=True)
    # parent = serializers.IntegerField()
    # replies = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')  

    # def get_replies(self, comment):
        # replies = comment.replies.all()
        # serializer = CommentSerializer(replies, many=True)
        # return serializer.data
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'author', 'created_at', 'updated_at')


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')  
    creator_id = serializers.ReadOnlyField(source='creator.id')  
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['creator', 'creator_id','created_at']

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)
