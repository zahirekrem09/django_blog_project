from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentFrom
from django.contrib import messages


@login_required(login_url="account_login")
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        "posts": posts
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="account_login")
def addarticle(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Makale Başarı ile Oluşturuldu")
        return redirect("dashboard")
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
        return redirect("dashboard")
    return render(request, "update.html", {"form": form})


@login_required(login_url="account_login")
def deleteArticle(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Makale Başarı ile Silindi")
    return redirect("dashboard")


def addComment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        new_comment = Comment(comment_author=comment_author,
                              comment_content=comment_content)
        new_comment.post = post
        new_comment.save()
    return redirect("/articles/post/" + str(id))
    # return redirect(reverse("post", kwargs={"id": id}))


def detail(request, id):
    post = Post.objects.filter(id=id).first()
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()

    return render(request, "post.html", {"post": post, "comments": comments})
