# from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, SentenceViewSet
'''
urlpatterns = (
    path('article/', ArticleAPIView.as_view()),
    path('relation/', RelationAPIView.as_view()),
)
'''
router = SimpleRouter()
router.register('article', ArticleViewSet, base_name='articles')
# router.register('relation', RelationViewSet, base_name='relations')
router.register('sentence', SentenceViewSet, base_name='sentences')
# router.register('entity', EntityViewSet, base_name='entity')
urlpatterns = router.urls
