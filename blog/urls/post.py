
from django.urls import path, include
from django.conf.urls import url
#from blog.views.post import BlogPageView
from blog.views.article import (dashboard, addarticle,
                                updateArticle, deleteArticle,
                                detail, articles,
                                favorite_post, new_add_comment, get_child_comment_form, add_or_remove_favorite)
urlpatterns = [
    path('<str:filter_by>', view=articles, name="articles"),
    #path('', BlogPageView.as_view(), name='articles'),
    #path('post/<int:id>', BlogDetailView.as_view(), name='post'),
    path('post/<int:id>/', view=detail, name='post'),

    # slug için id yazan yerdeki yerlere slug yazılıcak
    #path('post/<slug:slug>/', view=detail, name='post'),
    #path('dashboard/', view=dashboard, name="dashboard"),
    path('dashboard/<str:filter_by>', view=dashboard, name="dashboard"),
    path('addarticle/', view=addarticle, name="addarticle"),
    path('update/<int:id>', view=updateArticle, name="update"),
    path('delete/<int:id>', view=deleteArticle, name="delete"),
    #path('comment/<int:id>', view=addComment, name="comment"),

    #path('get-child-comment-form',view=get_child_comment_form, name="get-child-comment-form"),
    url(r'^get-child-comment-form/$', view=get_child_comment_form,
        name='get-child-comment-form'),
    url(r'^new-add-comment/(?P<pk>[0-9]+)/(?P<model_type>[\w]+)/$',
        view=new_add_comment, name='new-add-comment'),

    path('add-remove-favorite/<int:id>',
         view=add_or_remove_favorite, name='add-remove-favorite'),


    #path('new-add-comment/<int:id>/<str:model_type>',view=new_add_comment, name="new-add-comment"),

    path('post/<int:id>/favorite_post/',
         view=favorite_post, name='favorite_post'),

]
