from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('wine-viewset', views.WineViewSet)

urlpatterns = [
    url(r'^wine-view/', views.WineApiView.as_view()),
    url(r'', include(router.urls))
]