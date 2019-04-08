from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from accounts.models import NUser
from .forms import CommentForm
import json
from django.db.models import Count


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post, delete=False)
        postAuthor = get_object_or_404(NUser, user=post.author)
        relatedPosts = post.categories.all()[0].posts.all()
        hotest = Post.objects.all().order_by("date")[:5]
        context.update({
            'post': post,
            'comments': comments,
            'author': postAuthor,                        # lcount main Likes count.
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


class MainPage(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latestPosts'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        headerpost = Post.objects.all().order_by("date")[:3]
        latestposts = Post.objects.all().order_by("date")
        creator = User.objects.get(username="snow")
        popularposts = Post.objects.annotate(num_of_commets=Count("comments")).order_by('-num_of_commets')
        categories = PostCategory.objects.all()
        tags = Tag.objects.all()
        context.update({
            'headerPost': headerpost,
            'latestPosts': latestposts,
            'creator': creator,
            'popularPosts': popularposts,
            'categories': categories,
            'tags': tags,
        })


def autocomplateModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Post.objects.filter(title__startswith=q)
        results = []
        for r in search_qs:
            results.append(r.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)