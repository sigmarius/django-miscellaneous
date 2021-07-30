from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Please write the title', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='Alias')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Please write the content')
    is_published = forms.BooleanField(label='Published?', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Category is not choosen')
