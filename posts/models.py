from django.db import models
from django.contrib.auth.models import User


class PostCategory(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Tag(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return '#{}'.format(self.name)


class Post(models.Model):
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_created=True)
    body = models.TextField()
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(PostCategory, help_text="Please enter post categories", related_name='posts')
    tags = models.ManyToManyField(Tag, help_text='Please select or just created tags related to this post.')

    def __str__(self):
        return 'Post {0} - user {1}'.format(self.id, self.author.username)

    def display_author(self):
        return self.author.username

    def display_categories(self):
        return ', '.join([cat.title for cat in self.categories.all()])

    def get_full_name(self):
        return self.author.first_name + ' ' + self.author.last_name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Likes')
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=200)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment : {0}, User {1}'.format(self.id, self.user.username)

    def get_full_name(self):
        return self.user.first_name + self.user.last_name

