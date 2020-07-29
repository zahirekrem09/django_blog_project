from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from blog.models import Post, Comment, NewComment, FavoriteBlog, Category
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
# from django.utils.text import slugify


@login_required(login_url="account_login")
def addarticle(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        post = form.save(commit=False)
        post.author = request.user
        post.save()

        # slug ekleme(1. method)
        # post.save(commit=False)
        # post.slug = slugify(post.title.replace('ı','i'))
        # post.save()
        messages.success(request, "Article Created Successfully")
        return HttpResponseRedirect(reverse('dashboard', kwargs={"filter_by": 'all'}))
        # return redirect("dashboard", filter_by="all")
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
        messages.success(request, "Article Updated Successfully")
        return HttpResponseRedirect(reverse('dashboard', kwargs={"filter_by": 'all'}))
        # return redirect("dashboard", filter_by="all")
    return render(request, "update.html", {"form": form})


@login_required(login_url="account_login")
def deleteArticle(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Article Successfully Deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect("dashboard", filter_by="all")


def detail(request, id):
    form = CommentForm()
    # post = Post.objects.filter(id=id).first()
    post = get_object_or_404(Post, id=id)
    post.views = post.views + 1
    post.save()
    # comments = post.comments.all()
    articles_list = Post.objects.all()[:5]
    print(articles_list)

    category_list = Category.objects.all()

    print(category_list)

    # return render(request, "post.html", {"post": post, "form": form})
    return render(request, "post2.html", {"post": post, "form": form, "articles_list": articles_list, "category_list": category_list})


def articles(request, filter_by):
    articles_list = Post.objects.all()
    # Search
    keyword = request.GET.get("keyword")
    if keyword:
        # articles_list = Post.objects.filter(title__contains=keyword)
        articles_list = Post.objects.filter(
            Q(title__contains=keyword) |
            Q(content__contains=keyword)
        ).distinct()
    if filter_by == 'favorites':
        articles_list = []
        for article in FavoriteBlog.objects.filter(user=request.user):
            articles_list.append(article.post)

            # Search
        if keyword:
            article_id = []
            for article in FavoriteBlog.objects.filter(user=request.user):
                article_id.append(article.post.id)
                print(article_id)
                articles_list = Post.objects.filter(
                    Q(id__in=article_id) & (Q(title__contains=keyword) | Q(content__contains=keyword))).distinct()

        # return render(request,"articles.html",{"articles":articles})

    # Paginator
    paginator = Paginator(articles_list, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # return render(request, "articles.html", {"articles": articles, 'filter_by': filter_by})
    return render(request, "articles2.html", {"articles": articles, 'filter_by': filter_by})


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


@login_required(login_url="account_login")
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


@login_required(login_url="account_login")
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
    #messages.success(request, "Commet succesfuly")

    return JsonResponse(data=data)


@login_required(login_url="account_login")
def add_or_remove_favorite(request, id):

    post = get_object_or_404(Post, id=id)
    favori_blog = FavoriteBlog.objects.filter(
        post=post, user=request.user)
    if favori_blog.exists():
        favori_blog.delete()
    else:
        FavoriteBlog.objects.create(post=post, user=request.user)
        post.is_favorite = True
        post.save()
    count = post.get_favorite_count()
    #data.update({'count': count})
    if count > 0:
        post.is_favorite = True
    else:
        post.is_favorite = False
    post.save()
    # return JsonResponse(data=data)
    # favori_blog_list = []
    # favori_blog_list_post = []
    # for i in FavoriteBlog.objects.all():
    #     favori_blog_list.append(i.user.username)
    #     favori_blog_list_post.append((i.post.title, i.post.is_favorite))
    # print(favori_blog_list)
    # print(favori_blog_list_post)

    messages.success(request, "Article Successfully Added to Favorites")
    # return render(request, "articles.html", {"articles": articles})
    # return redirect(reverse("blog:post", kwargs={"id": id}))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
