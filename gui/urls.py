from django.contrib import admin
from django.urls import path,include
from gui import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="home"),
    path("predict",views.prr,name="pred"),
]
