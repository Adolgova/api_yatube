from django.urls import include, path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from api import views

v1_router = DefaultRouter()

v1_router.register(r'posts', views.PostViewSet)
v1_router.register(r'groups', views.GroupViewSet)
v1_router.register(r'^posts/(?P<post_id>\d+)/comments', views.CommentViewSet)
v1_router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('v1/api-token-auth/', auth_views.obtain_auth_token),
    path('v1/', include(v1_router.urls))
]
