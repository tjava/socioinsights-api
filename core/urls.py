from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
]

admin.site.site_header = "Socio Insights Api"
admin.site.site_title = "Socio Insights Api Panel"
admin.site.index_title = "Welcome to Socio Insights Api Panel"
