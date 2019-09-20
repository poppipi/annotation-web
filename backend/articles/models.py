from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=250)
    sen_num = models.IntegerField()
    is_yuqing = models.IntegerField()
    source = models.CharField(max_length=200)
    introduce = models.TextField()
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.title
