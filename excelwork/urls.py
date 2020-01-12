#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-01-12 20:22:56


from django.urls import path
from . import views


app_name = "excelwork"


urlpatterns = [
    path("删除/<int:pk>/", views.客户删除视图.as_view(), name="删除客户"),
]
