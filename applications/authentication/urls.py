from django.urls import include, path
from rest_framework import routers

from applications.authentication import views

router = routers.DefaultRouter()
router.register('auth', views.RegistrationViewSet, 'auth')

urlpatterns = [
    path('', include(router.urls)),

]