from rest_framework import serializers
from .models import Sentence


class SentenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = ('id', 'article_id', 'content', 'is_label')
