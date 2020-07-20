from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    subtitle = models.CharField(max_length=100, verbose_name="Alt Başlık")
    content = RichTextField(verbose_name="İçerik")
    author = models.ForeignKey(
        to="blog.User", on_delete=models.CASCADE, verbose_name="Yazar")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturma Tarihi")
    image = models.FileField(
        upload_to='images/', blank=True, null=True, verbose_name="İmage")

    class Meta:
        # olusturma tarihine göre sıralama
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Yazar")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturma Tarihi")

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment_author
