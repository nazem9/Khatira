from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="auther", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    title = models.CharField( max_length=200)
    body = models.TextField()
    def __str__(self) -> str:
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

class CommentLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now=True)