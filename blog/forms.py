from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('title', 'slug',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Вы не можете создать такой слаг.')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Слаг "{}" уже есть.'.format(new_slug))
        return new_slug


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=150, label='От кого')
    email = forms.EmailField(label='E-mail')
    to = forms.EmailField(label='Кому')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Комментарий')
