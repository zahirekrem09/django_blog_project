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
    comments = BlogComment.objects.filter(post=post, parent=None)
    # sadece replyler
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

        # context dic key göndermek mantıklı list olarqk
    context = {'post': post, 'comments': comments,
               'user': request.user, 'replyDict': replyDict}
    return render(request, 'post_detail.html', context)


# postCommentViews
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postId = request.POST.get('postId')
        post = Post.objects.get(sno=postId)
        parentSno = request.POST.get('parentSno')
        if parentSno == '':
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, 'Mesaj')
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)

            comment.save()
            messages.success(request, 'Mesaj reply')
    # ilgili post redirect yapılıcak
    return redirect(f'/blog/{post.slug}')
