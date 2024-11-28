from rest_framework import routers
from django.shortcuts import render
from django.urls import path, include
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index),  # Renderiza el index.html en la raíz
    path('api/projects', include(router.urls)),  # Incluye las rutas del API bajo /api/
]
