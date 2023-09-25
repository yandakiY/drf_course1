from django.urls import path
from django.contrib import admin
from rest_framework import routers
from core import views as views_core

router = routers.DefaultRouter();

urlpatterns = router.urls

urlpatterns += [
    path('admin/' , admin.site.urls),
    path('contact/' , views_core.ContactAPIView.as_view())
]
