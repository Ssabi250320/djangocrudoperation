from django import forms
from .models import student,personlinfo
from .models import *
from django.forms import inlineformset_factory
class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"
class personlinfoForm(forms.ModelForm):
    class Meta:
        model = personlinfo
        fields = "__all__"


