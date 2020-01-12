from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .  import models, forms
from excelwork.models import Excel, 客户
from openpyxl import load_workbook


class FileCreateView(LoginRequiredMixin, CreateView):
    queryset = Excel.objects.all()
    fields = ["file"]
    template_name = "django_netdisk/file_create.html"
    success_url = reverse_lazy('netdisk:file_list')

    def parse_excel(self, obj):
        """成功，返回None"""
        wb = load_workbook(obj.file.path)
        ws = wb.get_active_sheet()
        rows = ws.rows
        header = next(rows)
        if ['姓名', '下单时间', '联系方式', '购货时间'] != [x.value for x in header]:
            return "标题不正确"
        for index, row in enumerate(rows):
            try:
                客户.objects.create(
                    excel=obj,
                    姓名=row[0].value,
                    下单时间=row[1].value,
                    联系方式=row[2].value,
                    购货时间=row[3].value,
                )
            except Exception as e:
                return "第{}行不正确: {}".format(index, e)
                


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        res = self.parse_excel(self.object)
        if res:
            return HttpResponse(res)
        return super().form_valid(form)


class FileListView(LoginRequiredMixin, ListView):
    queryset = Excel.objects.all()

    def get_queryset(self):
        return models.File.objects.filter(
            user=self.request.user
        )

    def get_context_data(self):
        context = super().get_context_data()
        context["shared_files"] = Excel.objects.filter(
            receiver=self.request.user
        )
        return context


class FileDeleteView(LoginRequiredMixin, DeleteView):
    queryset = models.File.objects.all()
    success_url = reverse_lazy('netdisk:file_list')

    def get_queryset(self):
        return models.File.objects.filter(user=self.request.user)


class FileEditView(LoginRequiredMixin, UpdateView):
    fields = ["receiver"]
    success_url = reverse_lazy('netdisk:file_list')
    template_name = "django_netdisk/file_form.html"

    def get_queryset(self):
        return Excel.objects.filter(user=self.request.user)
