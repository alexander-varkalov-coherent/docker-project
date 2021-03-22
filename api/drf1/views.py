# Create your views here.
from rest_framework.viewsets import ModelViewSet

from drf1.models import Comment
from drf1.serializers import CommentSerializer


class APICommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
