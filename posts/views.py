from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post, Comment, Like

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'

    def get_context_data(self, **kwargs):
        context = super(PostViews, self).get_context_data(**kwargs)
        slug = self.kwargs['PostSlug']
        post = get_object_or_404(slug=slug)
        comments = Comment.objects.filter(post=post)
        likes = Like.objects.filter(post=post)
        likesCount = len(likes)
        context.update({
            'post': post,
            'comments': comments,
            'lcount': likesCount,   # lcount main Likes count.
        })
        return context
