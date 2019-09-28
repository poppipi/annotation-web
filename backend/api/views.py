# from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from articles.models import Article
from articles.serializers import ArticleSerializer
# from relations.models import Relation
# from relations.serializers import RelationSerializer
from sentences.models import Sentence
from sentences.serializers import SentenceSerializer
# from entity.models import Entity
# from entity.serializers import EntitySerializer
from .permissions import IsAuthenOrReadOnly
from users.serializers import UserSerializer


# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
