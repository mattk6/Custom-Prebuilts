"""
customPrebuilts/urls.py
Matthew Kruse
2025-04-13

customPrebuilts Urls
"""

from customPrebuilts import views
from rest_framework.routers import DefaultRouter
from django.urls import path

from customPrebuilts.views import PartsGPURetrieveUpdateDestroyView, PartsCPURetrieveUpdateDestroyView, \
    PartsMotherboardRetrieveUpdateDestroyView

router = DefaultRouter()
router.register("cpu", views.PartsCPUListCreateView)
router.register("gpu", views.PartsGPUListCreateView)
router.register("motherboard", views.PartsMotherboardListCreateView)

urlpatterns = router.urls

urlpatterns += [
    # Endpoints for detail, update, delete
    path('gpu/<int:pk>/', PartsGPURetrieveUpdateDestroyView.as_view(), name='gpu-detail'),
    path('cpu/<int:pk>/', PartsCPURetrieveUpdateDestroyView.as_view(), name='cpu-detail'),
    path('motherboard/<int:pk>/', PartsMotherboardRetrieveUpdateDestroyView.as_view(), name='motherboard-detail'),
]

