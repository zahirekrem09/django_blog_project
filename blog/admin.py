
from django.contrib import admin
from blog.models import (Post, Comment,
                         User, FavoriteBlog,
                         Interest, NewComment)

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NewComment)
admin.site.register(User)
admin.site.register(Interest)
admin.site.register(FavoriteBlog)

# slug için
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'publishing_date', 'slug']
#     list_display_links = ['publishing_date']
#     list_filter = ['publishing_date']
#     search_fields = ['title', 'content']
#     list_editable = ['title']

#     class Meta:
#         model = Post

# admin.site.register(Post, PostAdmin)
