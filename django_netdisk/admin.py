from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "createtime"]
