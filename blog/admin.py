
from django.contrib import admin
from blog.models import (Post, Comment,
                         User,
                         Interest)

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Interest)
