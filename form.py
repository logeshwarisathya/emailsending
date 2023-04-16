from django import forms
from cbvapp.models import Marks


class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields='__all__'

