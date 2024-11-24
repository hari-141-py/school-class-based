from log.models import School
from django import forms


class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name','address','population','faculty','details']

class EditSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name','address','population','faculty','details']