# from django.shortcuts import render
from rest_framework import viewsets
from articles.models import Article
from articles.serializers import ArticleSerializer
# from relations.models import Relation
# from relations.serializers import RelationSerializer
from sentences.models import Sentence
from sentences.serializers import SentenceSerializer
# from entity.models import Entity
# from entity.serializers import EntitySerializer

# from .permissions import IsAuthenOrReadOnly

# Create your views here.


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


'''
class RelationViewSet(viewsets.ReadOnlyModelViewSet):
    # perimission_classes = (IsAuthenOrReadOnly,)
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
'''


class SentenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


'''
class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
'''
