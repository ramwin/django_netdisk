from django.db import models

# Create your models here.

from django_netdisk.models import File
from django.contrib.auth import get_user_model


User = get_user_model()


class Excel(File):
    receiver = models.ForeignKey(
        User, verbose_name="接收人", on_delete=models.CASCADE, related_name="excels", null=True)

    class Meta:
        verbose_name = verbose_name_plural = "Excel文件"


class 客户(models.Model):
    excel = models.ForeignKey(Excel, on_delete=models.CASCADE)
    姓名 = models.CharField(max_length=31)
    下单时间 = models.DateTimeField()
    联系方式 = models.CharField(max_length=31)
    购货时间 = models.DateTimeField()

    @property
    def 处理人(self):
        return self.excel.receiver
