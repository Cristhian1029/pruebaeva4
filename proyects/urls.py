from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet
from .views import home 
router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls + [
    path('', home, name='home'),  
]