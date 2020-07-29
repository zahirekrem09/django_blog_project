from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.commnet[0:13] + '....' + self.user.email


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'post_detail.html', context)


# postCommentViews
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postId = request.POST.get('postId')
        post = Post.objects.get(sno=postId)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, 'Mesaj')
    # ilgili post redirect yapılıcak
    return redirect(f'/blog/{post.slug}')
