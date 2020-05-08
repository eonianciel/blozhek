from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, db_index=True, verbose_name='Заголовок')
    text = models.TextField(blank=True, db_index=True, verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #slug = models.SlugField(max_length=150, unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{}'.format(self.title)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    class Meta:
        ordering = ['-published_date']



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=250, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
