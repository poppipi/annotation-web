from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'sen_num', 'is_yuqing', 'source',
                  'introduce', 'word')
