from rest_framework import serializers
from .models import Post, Comment


# class NestedCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'content', 'author', 'created_at', 'updated_at' , 'parent')


class CommentSerializer(serializers.ModelSerializer):
    # replies = NestedCommentSerializer(many=True, required=False ,read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')  

    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'author','author_id' , 'created_at', 'updated_at')
        read_only_fields = ['author', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')  
    creator_id = serializers.ReadOnlyField(source='creator.id')  
    comment = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['creator', 'creator_id','created_at', "likes_count"]

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    def get_likes_count(self, obj):
        return obj.likes.count()