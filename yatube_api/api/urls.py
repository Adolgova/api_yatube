from api import views
from django.urls import include, path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('', include(router.urls))
]
