from django.urls import path, include
from rest_framework import routers

from .views import (TitlesViewSet, CategoriesViewSet, GenresViewSet,
                    ReviewViewSet, CommentViewSet)

router_v1 = routers.DefaultRouter()
router_v1.register(r'titles', TitlesViewSet, basename='titles')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
]
