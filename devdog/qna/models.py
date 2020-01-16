from django.db import models
from user.models import User
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)
    people = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    article_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    
    def __str__(self):
        return self.content
