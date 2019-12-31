from django import forms
from . import models

class FileForm(forms.ModelForm):

    class Meta:
        model = models.File
        fields = ["file"]

    def save(self):
        import ipdb
        ipdb.set_trace();
