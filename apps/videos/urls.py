from django.urls import path
from .views import *


urlpatterns = [
    path('', Video_list.as_view(), name='videos'),
    path('genres/', Genre_list.as_view(), name='genres'),
    path('tegs/', Teg_list.as_view(), name='tags'),
    path('video/<int:pk>', Video_detail.as_view(), name='video_detail'),
    path('video/<int:pk>/like', like_video, name='like_video'),
    path('video/<int:pk>/dislike', dislike_video, name='dislike_video'),
    path('video/<int:pk>/comment', add_comment, name='add_comment'),
    path('comment/<int:pk>/like', like_comment, name='like_comment'),
    path('comment/<int:pk>/dislike', dislike_comment, name='dislike_comment'),
]
