from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Comment


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=1_000_000, required=False)
    genres = forms.JSONField(required=False, widget=forms.HiddenInput())
    teg = forms.JSONField(required=False, widget=forms.HiddenInput())
    
    CHOICES = (('Дате', 'date'),('просмотры', 'views'), ('рейтинг', 'rating'))
    sort_type = forms.ChoiceField(choices=CHOICES, required=False)
    

class CommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea(attrs={
                    'rows': "3", 'class': "comment-field input", 'placeholder': "Коментраий..."})
    
    class Meta:
        model = Comment
        fields = ('text', 'video', 'user')
    