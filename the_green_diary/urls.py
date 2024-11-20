from django.contrib import admin
from django.urls import path, include
from green_diary.views import HomeView

# change api/ to home since it's the home page url.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("api/", include("green_diary.urls")),
]
