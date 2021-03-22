from django.urls import path

from web1.views import all_comments, create_comment, edit_comment, delete_comment

urlpatterns = [
    path('', all_comments, name='comments'),
    path('create_comment', create_comment, name='create-comment'),
    path('edit_comment/<int:pk>', edit_comment, name='edit-comment'),
    path('delete_comment/<int:pk>', delete_comment, name='delete-comment'),
]
