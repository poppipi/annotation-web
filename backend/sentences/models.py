from django.db import models
from articles.models import Article
# Create your models here.


class Sentence(models.Model):
    article_id = models.ForeignKey(Article, on_delete='CASCADE')
    content = models.TextField()
    is_label = models.IntegerField()

    def __str__(self):
        return self.content[:10]
