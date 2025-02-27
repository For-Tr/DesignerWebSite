"""
URL configuration for notes_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from django.urls import path, re_path, include

from notes_back import settings
from users.views import UserViewSet, verify_email, CustomTokenObtainPairView, info, edit_user

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'api/user', UserViewSet)

urlpatterns = [
                  path(r'admin/', admin.site.urls),
                  path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/', include(router.urls)),
                  path('api/verify', verify_email, name='verify-email'),
                  path('verification-success/', TemplateView.as_view(template_name='verification_success.html'),
                       name='verification-success'),
                  path('api/getuser/', info),
                  path('api/edit_user/', edit_user),
                  path('api/notes/', include('notes.urls', namespace='notes')),
                  path('social-auth/', include('social_django.urls', namespace='social')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 媒体文件路径
urlpatterns += router.urls
