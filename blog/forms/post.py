from django import forms
from blog.models.post import Post, Comment, NewComment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "subtitle", "content", "image", "is_favorite")


# class CommentFrom(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ("comment_author", "comment_content")
#         widgets = {
#             'comment_author': forms.TextInput(attrs={
#                 'placeholder': 'Author'
#             }),
#             'comment_content': forms.TextInput(attrs={
#                 'placeholder': 'Content'
#             })
#         }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = NewComment
#         fields = ['comment_content']

#     def __init__(self, *args, **kwargs):
#         super(CommentForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs = {'class': 'form-control'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['icerik']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
