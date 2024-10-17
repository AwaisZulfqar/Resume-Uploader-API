from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProfileView
from resumeAPI import views
router = DefaultRouter()

router.register('profileapi',views.ProfileView,basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    
]
