from django.db import models
from articles.models import Article
# Create your models here.


class Sentence(models.Model):
    article_id = models.ForeignKey(Article, on_delete='CASCADE')
    content = models.TextField()
    entitys = models.TextField()
    label = models.TextField(null=True, blank=True)
    updatetime = models.DateTimeField(auto_now=True)
    uid = models.IntegerField(null=True, blank=True)
    is_Process = models.IntegerField()

    def __str__(self):
        return self.content[:10]
