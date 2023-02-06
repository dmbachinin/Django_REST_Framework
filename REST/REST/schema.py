import graphene
from graphene_django import DjangoObjectType
from authors.models import Book, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.UUID(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))

    def resolve_books(self, info):
        return Book.objects.all()

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()
        if name:
            books = books.filter(author__first_name=name)
        return books


class AuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.UUID()
        first_name = graphene.String()
        last_name = graphene.String()
        birthday = graphene.Int()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, first_name, last_name, birthday):
        author = Author.objects.get(pk=id)
        author.first_name = first_name
        author.last_name = last_name
        author.birthday = birthday
        author.save()
        return AuthorMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
