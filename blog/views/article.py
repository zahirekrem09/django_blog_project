from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from blog.models import Post, Comment, NewComment
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
#from django.utils.text import slugify


@login_required(login_url="account_login")
def addarticle(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        post = form.save(commit=False)
        post.author = request.user
        post.save()

        # slug ekleme(1. method)
        # post.save(commit=False)
        #post.slug = slugify(post.title.replace('ı','i'))
        # post.save()

        messages.success(request, "Makale Başarı ile Oluşturuldu")
        return redirect("dashboard", filter_by="all")
    return render(request, "addarticle.html", {"form": form})


@login_required(login_url="account_login")
def updateArticle(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)

    form = PostForm(request.POST or None,
                    request.FILES or None, instance=post)
    if form.is_valid():

        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Makale Başarı ile Güncellendi")
        return redirect("dashboard", filter_by="all")
    return render(request, "update.html", {"form": form})


@login_required(login_url="account_login")
def deleteArticle(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Makale Başarı ile Silindi")
    return redirect("dashboard", filter_by="all")


# def addComment(request, id):
#     post = get_object_or_404(Post, id=id)

#     if request.method == "POST":
#         comment_author = request.POST.get("comment_author")
#         comment_content = request.POST.get("comment_content")

#         if comment_author != "" and comment_content != "":

#             new_comment = Comment(comment_author=comment_author,
#                                   comment_content=comment_content)
#             new_comment.post = post
#             new_comment.save()
#             messages.success(request, "Comment Successfully Added")
#         else:
#             messages.warning(request, "Please fill in the fields.")
#     return redirect("/articles/post/" + str(id))
#     # return redirect(reverse("post", kwargs={"id": id}))


def detail(request, id):
    form = CommentForm()
    #post = Post.objects.filter(id=id).first()
    post = get_object_or_404(Post, id=id)
    #comments = post.comments.all()

    return render(request, "post.html", {"post": post, "form": form})


def articles(request):
    articles_list = Post.objects.all()
    # Search
    keyword = request.GET.get("keyword")
    if keyword:
        #articles_list = Post.objects.filter(title__contains=keyword)
        articles_list = Post.objects.filter(
            Q(title__contains=keyword) |
            Q(content__contains=keyword)
        ).distinct()

        # return render(request,"articles.html",{"articles":articles})

    # Paginator
    paginator = Paginator(articles_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, "articles.html", {"articles": articles})


def favorite_post(request, id):
    post = get_object_or_404(Post, id=id)
    try:
        if post.is_favorite:
            post.is_favorite = False
        else:
            post.is_favorite = True
        post.save()
    except (KeyError, Post.DoesNotExist):
        return redirect("dashboard", filter_by="all")
    else:
        return redirect("dashboard", filter_by="all")


# @login_required(login_url="account_login")
# def dashboard(request):
#     posts = Post.objects.filter(author=request.user)
#     context = {
#         "posts": posts
#     }
#     return render(request, "dashboard.html", context)


@login_required(login_url="account_login")
def dashboard(request, filter_by):
    try:
        post_ids = []
        for post in Post.objects.filter(author=request.user):
            post_ids.append(post.id)
        author_posts = Post.objects.filter(id__in=post_ids)
        if filter_by == 'favorites':
            author_posts = author_posts.filter(is_favorite=True)
    except Post.DoesNotExist:
        users_songs = []
    return render(request, 'dashboard.html', {
        'posts': author_posts,
        'filter_by': filter_by,
    })


def get_child_comment_form(request):
    data = {'form_html': ''}
    pk = request.GET.get('comment_pk')
    comment = get_object_or_404(NewComment, pk=pk)
    form = CommentForm()
    form_html = render_to_string('comment/comment-child-comment-form.html', context={
        'form': form,
        'comment': comment
    }, request=request)

    data.update({
        'form_html': form_html
    })

    return JsonResponse(data=data)


def new_add_comment(request, pk, model_type):
    data = {'is_valid': True, 'blog_comment_html': '', 'model_type': model_type}
    nesne = None
    all_comment = None
    form = CommentForm(data=request.POST)

    if model_type == 'post':
        nesne = get_object_or_404(Post, pk=pk)
    elif model_type == 'comment':
        nesne = get_object_or_404(NewComment, pk=pk)
    else:
        raise Http404

    if form.is_valid():
        icerik = form.cleaned_data.get('icerik')
        NewComment.add_comment(nesne, model_type, request.user, icerik)
    # yorum ekranını güncelleyeceğimiz yer.
    if model_type == 'comment':
        # burada eğer gelen nesne comment ise blogu almak için.
        nesne = nesne .content_object
    # tüm yorumlarını tekrardan çekiyoruz.
    comment_html = render_to_string('comment/comment-list-partial.html', context={
        'post': nesne
    })

    data.update({
        'blog_comment_html': comment_html
    })

    return JsonResponse(data=data)
