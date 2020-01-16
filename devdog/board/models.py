from django.db import models
from user.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    aritcle_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content_c = models.TextField()
    def __str__(self):
        return self.content_c
    