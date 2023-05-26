from django import forms
from ckeditor.widgets import CKEditorWidget

from blog.models import Article

class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['title', 'description', 'body']