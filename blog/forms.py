from django import forms

from .models import Post, Send

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class TestForm(forms.ModelForm):

    class Meta:
        model = Send
        fields = ('textin',)

class TestForm1(forms.Form):
    textin = forms.CharField(max_length=100)
