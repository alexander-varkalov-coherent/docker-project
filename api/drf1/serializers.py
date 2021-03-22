from rest_framework import serializers

from drf1.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'firstname',
            'lastname',
            'age',
            'text',
        )
