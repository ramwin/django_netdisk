import pathlib
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model()


class File(models.Model):
    file = models.FileField(upload_to="netdisk_file/%Y/%m/%d")
    groups = models.ManyToManyField(Group)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "用户上传的文件"

    def display(self):
        return pathlib.Path(self.file.path).name
