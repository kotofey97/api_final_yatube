from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet

appname = 'api'
router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename="comments")

urlpatterns = [
    path('v1/follow/', FollowViewSet.as_view(), name='follow'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
