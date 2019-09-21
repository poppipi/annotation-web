from django.db import models

# Create your models here.


class Article(models.Model):
    url = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    is_yuqing = models.IntegerField()
    source = models.CharField(max_length=200)
    introduce = models.TextField()
    content = models.TextField()
    word = models.CharField(max_length=50)
    content_sentense_parser = \
        models.TextField(null=True, blank=True)
    content_entity = \
        models.TextField(null=True, blank=True)
    content_svos = \
        models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
