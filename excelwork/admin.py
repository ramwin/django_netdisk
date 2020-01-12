from django.contrib import admin
from . import models


@admin.register(models.客户)
class 客户Admin(admin.ModelAdmin):
    list_display = ["id", "姓名", "处理人"]
