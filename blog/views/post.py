from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Class tabanlı views


# class BlogPageView(ListView):
#     # paginations
#     paginate_by = 2
#     model = Post
#     template_name = 'articles.html'


# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'post.html'


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

##blog detail views örneği
# def blog_detail(request, blog_slug):
#     blog = get_object_or_404(Blog, slug=blog_slug)
#     session_key = 'blog_views_{}'.format(blog.slug)
#     if not request.session.get(session_key):
#         blog.blog_views += 1
#         blog.save()
#         request.session[session_key] = True

#     content_type = ContentType.objects.get_for_model(Blog)
#     object_id = blog.id
#     # look at CommentManager as well
#     comments = Comment.objects.filter(content_type=content_type, object_id=object_id).filter(parent=None)


#     initial_data = {
#         'content_type':blog.get_content_type,
#         'object_id': blog.id
#     }

#     form = CommentForm(request.POST or None, initial=initial_data)

#     if form.is_valid():
#         c_t = form.cleaned_data.get('content_type')
#         content_type = ContentType.objects.get(model = c_t)
#         obj_id = form.cleaned_data.get('object_id')
#         content = form.cleaned_data.get('content')
#         parent_obj = None

#         try:
#             parent_id = int(request.POST.get('parent_id'))
#         except:
#             parent_id = None

#         if parent_id:
#             parent_qs = Comment.objects.filter(id=parent_id)
#             if parent_qs.exists() and parent_qs.count() == 1:
#                 parent_obj = parent_qs.first()

#         new_comment = Comment.objects.create(
#             user = request.user,
#             content_type = content_type,
#             object_id = obj_id,
#             content = content,
#             parent=parent_obj,
#         )

#         return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

#     context = {
#         'blog': blog,
#         'categories': get_category_count(),
#         'comments':comments,
#         'form':form,
#     }

#     return render(request, 'blogs/blog-detail.html', context)
