"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from authors.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, MyApiView

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('my', MyApiView, basename='my')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="api/")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('myapi/', MyApiView.as_view({'get': 'list'}))
]
