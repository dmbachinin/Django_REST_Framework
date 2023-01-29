from django.test import TestCase
import json

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import Author, Book


class TestAuthorViewSet(TestCase):

    # Use APIRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {'first_name': 'САНЯ', 'last_name': 'ЕГОРОВ', 'birthday': 2003})
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {'first_name': 'САНЯ', 'last_name': 'ЕГОРОВ', 'birthday': 2003})
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Use APIClient
    def test_get_detail(self):
        author = Author.objects.create(first_name='САНЯ', last_name='ЕГОРОВ', birthday=2003)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_quest(self):
        author = Author.objects.create(first_name='САНЯ', last_name='ЕГОРОВ', birthday=2003)
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}/', {'first_name': 'DD', 'last_name': 'VV', 'birthday': 2222})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='САНЯ', last_name='ЕГОРОВ', birthday=2003)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        # Авторизация клиента
        client.login(username='admin', password='admin')
        response = client.put(f'/api/authors/{author.id}/', {'first_name': 'DD', 'last_name': 'VV', 'birthday': 2222})

        author = Author.objects.get(pk=author.id)

        self.assertEqual(author.first_name, 'DD')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()


# Use APISimpleTestCase
class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(9), 3)


# Use APITestCase
class TestBookViewSet(APITestCase):

    def test_get_lists(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_book_admin(self):
        author = Author.objects.create(first_name='САНЯ', last_name='ЕГОРОВ', birthday=2003)
        book = Book.objects.create(name='Book1')
        book.author.add(author)
        book.save()

        # book = mixer.blend(Book)

        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        self.client.login(username='admin', password='admin')

        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Book2', 'author': author.id})

        book = Book.objects.get(pk=book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.name, 'Book2')
        self.client.logout()
