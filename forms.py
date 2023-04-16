from django import forms
from myapp.models import Registration

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model=Registration
        # fields='__all__'------------it will show all the heading in the table
        fields=['username','first_name','last_name','email','phone','gender','password']