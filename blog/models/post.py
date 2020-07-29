from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from blog.choices import CategoryChoices


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    subtitle = models.CharField(max_length=100, verbose_name="Sub Title")
    content = RichTextField(verbose_name="İçerik")
    author = models.ForeignKey(
        to="blog.User", on_delete=models.CASCADE, verbose_name="Author")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created Date")
    image = models.FileField(
        upload_to='images/', blank=True, null=True, verbose_name="Post İmage", default="/images/post-sample-image.jpg")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    category = models.ManyToManyField(to=Category)
    views = models.IntegerField(default=0)

    is_favorite = models.BooleanField(default=False)

    # slug = models.SlugField(unique=True,editable=False,max_length=150)

    # def get_unique_slug(self):
    #  slug = slugify(self.title.replace('ı', 'i'))
    #  unique_slug = slug
    #  counter = 1
    #  while Post.objects.filter(slug=unique_slug).exists():
    #      unique_slug = f'{slug}-{counter}'
    #      counter += 1
    #  return unique_slug

    # def save(self, *args, **kwargs):
    #    self.slug = self.get_unique_slug()
    #    return super(Post, self).save(*args, **kwargs)

    class Meta:
        # olusturma tarihine göre sıralama
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_blog_new_comment(self):
        content_type = ContentType.objects.get_for_model(self)
        object_id = self.id
        all_comment = NewComment.objects.filter(
            content_type=content_type, object_id=object_id)
        return all_comment

    def get_blog_comment(self):
        # gönderiye ait tüm yorumları bana veren fonksiyon
        return self.comment.all()

    def get_blog_comment_count(self):
        #b = NewComment.objects.filter(object_id=self.id)
        all_child_comment_list = []
        for i in list(self.get_blog_new_comment()):
            if i.is_parent:
                for j in list(i.get_child_comment()):
                    all_child_comment_list.append(j.get_child_comment())
                #content_type = ContentType.objects.get_for_model(i.__class__)
                #all_child_comment_list.append(NewComment.objects.filter(content_type=content_type, object_id=i.id))
        # return len(self.get_blog_new_comment())
        return len(self.get_blog_new_comment()) + len(all_child_comment_list)

    def get_favorite_count(self):
        favori_sayisi = self.favorite_blog.count()
        return favori_sayisi

    def get_added_favorite_user_as_object(self):
        data_list = []
        qs = self.favorite_blog.all()
        for obj in qs:
            data_list.append(obj.user)
        return data_list

    def get_category(self):
        return self.category.all().first()


# class Comment(models.Model):
#     post = models.ForeignKey(
#         Post, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
#     comment_author = models.CharField(max_length=50, verbose_name="Yazar")
#     comment_content = models.CharField(max_length=200, verbose_name="Yorum")
#     comment_date = models.DateTimeField(
#         auto_now_add=True, verbose_name="Oluşturma Tarihi")

#     is_favorite = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['-comment_date']

#     def __str__(self):
#         return self.comment_author

class Comment(models.Model):
    user = models.ForeignKey(to="blog.User", null=True,
                             default=1, related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, null=True, related_name='comment', on_delete=models.CASCADE)
    # comment = models.ForeignKey(to='self', null=True)

    icerik = models.TextField(verbose_name='Yorum',
                              max_length=1000, blank=False, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return "%s %s" % (self.user, self.post)


class NewComment(models.Model):
    user = models.ForeignKey(
        to="blog.User", null=True, default=1, related_name='+', on_delete=models.CASCADE)
    is_parent = models.BooleanField(default=False)

    content_type = models.ForeignKey(
        to=ContentType, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    icerik = models.TextField(
        verbose_name='Yorum', max_length=1000, blank=False, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} {self.content_type.model}"

    class Meta:
        verbose_name_plural = "iç içe yorum"

    @ classmethod
    def add_comment(cls, nesne, model_type, user, icerik):
        content_type = ContentType.objects.get_for_model(nesne.__class__)
        cls.objects.create(user=user, icerik=icerik,
                           content_type=content_type, object_id=nesne.id)
        if model_type == 'comment':
            nesne.is_parent = True
            nesne.save()

    def get_child_comment(self):
        if self.is_parent:
            content_type = ContentType.objects.get_for_model(self.__class__)
            all_child_comment = NewComment.objects.filter(
                content_type=content_type, object_id=self.id)
            return all_child_comment
        return None


class FavoriteBlog(models.Model):
    user = models.ForeignKey(to="blog.User", null=True,
                             default=1, related_name='favorite_blog', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, null=True, related_name='favorite_blog', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Favorilere Eklenen Gönderiler'

    def __str__(self):
        return "%s %s" % (self.user, self.post)


# class Category(models.Model):
#     name = models.PositiveIntegerField(
#         null=True, choices=CategoryChoices.CHOICES)
#     post = models.ForeignKey(
#         Post, null=True, related_name='category', on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = "Categories"

#     def __str__(self):
#         return self.name
