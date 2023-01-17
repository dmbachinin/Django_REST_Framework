from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    filterset_fields = ["first_name", "last_name"]
    pagination_class = AuthorPaginator


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class MyApiView(ViewSet):

    # get
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def HI(self, request):
        return Response({"data": "HI"})
