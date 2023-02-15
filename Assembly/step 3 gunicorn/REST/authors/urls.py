from django.urls import path
from authors.views import MyApiView


app_name = 'authors'
urlpatterns = [
    path('', MyApiView.as_view({'get': 'list'})),
]
