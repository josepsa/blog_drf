from . import views
from rest_framework import routers
from django.urls import path,include

router=routers.DefaultRouter()
router.register(r'fetch',views.PostViewSet)



urlpatterns=[
    path('',include(router.urls)),
]