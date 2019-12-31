from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .  import models, forms


class FileCreateView(LoginRequiredMixin, CreateView):
    queryset = models.File.objects.all()
    fields = ["file"]
    template_name = "django_netdisk/file_create.html"
    success_url = reverse_lazy('netdisk:file_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class FileListView(LoginRequiredMixin, ListView):
    queryset = models.File.objects.all()

    def get_queryset(self):
        return models.File.objects.filter(user=self.request.user)


class FileDeleteView(LoginRequiredMixin, DeleteView):
    queryset = models.File.objects.all()
    success_url = reverse_lazy('netdisk:file_list')

    def get_queryset(self):
        return models.File.objects.filter(user=self.request.user)
