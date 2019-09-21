from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'url', 'date', 'title', 'is_yuqing', 'source',
                  'introduce', 'content',  'word', 'content_sentence_parser',
                  'content_entity', 'content_svos')
