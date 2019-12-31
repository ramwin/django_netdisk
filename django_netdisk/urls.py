from django.urls import path
from . import views

app_name = "netdisk"

urlpatterns = [
    path("file_create/", views.FileCreateView.as_view(), name="file_create"),
    path("file_list/", views.FileListView.as_view(), name="file_list"),
    path("delete/<int:pk>/", views.FileDeleteView.as_view(), name="delete"),
]