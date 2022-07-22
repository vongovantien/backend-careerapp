from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('employers', views.EmployerViewSet, basename='employer')
router.register('posts', views.PostViewSet, basename='post')
router.register('users', views.UserViewSet, basename='user')
router.register('categories', views.CategoryList, basename="category")
router.register('candidates', views.CandidateViewSet, basename="candidate")
router.register('comments', views.CommentViewSet, basename="comment")
router.register('tags', views.TagViewSet, basename="tag")
router.register('locations', views.LocationViewSet, basename="location")

schema_view = get_schema_view(
    openapi.Info(
        title="CareerApp API",
        default_version='v1',
        description="APIs for Career Application",
        contact=openapi.Contact(email="vongovantien@gmail.com"),
        license=openapi.License(name="VO NGO VAN TIEN @2021"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('reset-password/', views.ResetPassword.as_view()),
    path('change-password/', views.ChangePassword.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
