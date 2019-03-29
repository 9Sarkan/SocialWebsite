from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from accounts.models import NUser
from .forms import CommentForm


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post, delete=False)
        likes = Like.objects.filter(post=post)
        postAuthor = get_object_or_404(NUser, user=post.author)
        relatedPosts = post.categories.all()[0].posts.all()
        hotest = Post.objects.all().order_by("date")[:5]
        context.update({
            'post': post,
            'comments': comments,
            'author': postAuthor,
            'lcount': len(likes),                           # lcount main Likes count.
            'ccount': len(comments),                        # ccount main comments count.
            'categories': post.categories,
            'tags': Tag.objects.all(),                      # send all tags
            'categories': PostCategory.objects.all(),       # send all categories
            'related': relatedPosts,
            'hotest': hotest,
            'form': CommentForm(),
        })
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            c = Comment.objects.create(user=request.user, post=Post.objects.get(slug=self.kwargs['slug']),
                                      body=message)
            c.save()
            return HttpResponseRedirect(reverse('PostView', kwargs={'slug': self.kwargs['slug']}))

