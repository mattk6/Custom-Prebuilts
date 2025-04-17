"""
customPrebuilts/urls.py
Matthew Kruse
2025-04-13

customPrebuilts Urls
"""

from customPrebuilts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("cpus", views.PartsCPUViewSet, 'parts-cpus')
router.register("gpus", views.PartsGPUViewSet, 'parts-gpus')
router.register("motherboards", views.PartsMotherboardViewSet, 'parts-motherboards')
router.register("games", views.GameViewSet, 'games')
router.register("game-specs", views.GameSpecViewSet, 'game-specs')

urlpatterns = router.urls

