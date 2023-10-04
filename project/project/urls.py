"""
URL configuration for project project.

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from lesson.views import LessonListView, ProductLessonsListView, ProductStatisticsViewSet

router = routers.DefaultRouter()
router.register(r'lesson', LessonListView)
router.register(r'products/(?P<product_id>\d+)', ProductLessonsListView, basename='productlessons')
router.register(r'products', ProductStatisticsViewSet, basename='productstatistics')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('products/<int:product_id>/lessons/', ProductLessonsListView.as_view({'get': 'list'}), name='product-lessons-list'),

]
