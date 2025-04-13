"""
urls.py
Matthew Kruse
2025-04-13

urls for the customPrebuilts app.
"""


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("customPrebuilts.urls"))
]
