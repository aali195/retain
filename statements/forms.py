from django import forms

from .models import Statement


class StatementForm(forms.ModelForm):

    class Meta:
        model = Statement
        fields = ('statement', 'image', 'question', 'answer')