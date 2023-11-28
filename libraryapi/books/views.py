from django.shortcuts import render
from books.models import Book
from books.serializers import  Bookserializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from books.serializers import Userserializer

class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class Userviewset(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = Userserializer
