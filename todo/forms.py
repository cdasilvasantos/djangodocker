# todo/forms.py
from django import forms
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']

    # Customize the description field
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))  # Adjust the 'rows' value as needed
