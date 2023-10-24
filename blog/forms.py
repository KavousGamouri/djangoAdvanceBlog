from django import forms
from django.contrib.auth.forms import UserChangeForm

from .models import Post, Contact, Comment, Newsletter


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'status', 'created_date']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'username', 'email', 'subject', 'message']


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'status']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
