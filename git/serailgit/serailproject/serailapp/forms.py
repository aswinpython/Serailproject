from django import forms
from.models import Serail
class SerailForm(forms.ModelForm):
    class Meta:
        model=Serail
        fields=['name','desc','year','img']
