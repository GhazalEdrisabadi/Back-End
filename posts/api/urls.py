from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostCreateAPIView)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
]
