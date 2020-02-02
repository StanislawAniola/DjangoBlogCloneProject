from django import forms
from group_app import models


class GroupForm(forms.ModelForm):

    class Meta():
        model = models.GroupModel
        fields = ['group_title', 'group_description']

        widgets = {
            'group_title': forms.TextInput(attrs={'class': 'form-control'}),
            'group_description': forms.TextInput(attrs={'class': 'form-control'}),
        }
