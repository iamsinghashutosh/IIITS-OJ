from django import forms
from django.forms import ModelForm
from froala_editor.widgets import FroalaEditor
from .models import Problem

class Statement(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['statement','constraint']



