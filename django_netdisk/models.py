from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class File(models.Model):
    file = models.FileField(upload_to="netdisk_file/%Y/%m/%d")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "用户上传的文件"