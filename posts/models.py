from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField()
    date = models.DateTimeField(auto_created=True)
    comment = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return 'Post {0} - user {1}'.format(self.id, self.user.username)


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

    def __str__(self):
        return 'Comment : {0}, User {1}'.format(self.id, self.user.username)

