from django.contrib import admin
from user.models import User
from board.models import Article,Comment
from qna.models import Question,Answer

# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)
