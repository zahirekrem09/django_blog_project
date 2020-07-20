from django import forms
from blog.models.post import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "subtitle", "content", "image")


class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_author", "comment_content")
        widgets = {
            'comment_author': forms.TextInput(attrs={
                'placeholder': 'Author'
            }),
            'comment_content': forms.TextInput(attrs={
                'placeholder': 'Content'
            })
        }
