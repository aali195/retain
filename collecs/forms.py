from django import forms

from .models import Collection


class NewCollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ('title', 'image', 'description', 'is_visible')

class EditCollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ('title', 'image', 'description')