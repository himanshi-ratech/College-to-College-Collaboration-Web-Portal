# forms.py
from django import forms
from .models import Post, Comment, Student_Detail

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author_name", "caption", "image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class StudentDetailForm(forms.ModelForm):
    class Meta:
        model= Student_Detail
        fields= ["name", "roll", "branch", "year", "dept", "email", "contact"]
