from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


from django.views.generic.edit import DeleteView


class 客户删除视图(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('netdisk:file_list')
    def get_queryset(self):
        return models.客户.objects.filter(excel__receiver=self.request.user)
