"""
    We need a form for created for the todos
"""
from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):
    """ Only want to set the ccs controls. """

    todo = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 10, 'rows': 5, 'class': 'form-control'}
    ))

    class Meta:
        """ Meta options go here. """
        model = ToDo
        exclude = ('created', 'compleated')
