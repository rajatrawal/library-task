from django.shortcuts import HttpResponse
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Genre, Author, Book
from . serializers import (GenreSerializer, AuthorSerializer, BookSerializer)
from django.contrib.auth.models import User
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import csv
from django.http import HttpResponse


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({
            'message': 'wrong credentials'
        }, status=HTTP_406_NOT_ACCEPTABLE)


class GenreAPI(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]


class BookAPI(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        author_user = Author.objects.filter(user=request.user)
        if (author_user.exists()):
            super().create(request, *args, **kwargs)
            return Response({
                'message': 'book object created '
            })
        return Response(
            {
                "status": 406,
                "message": "Invalid Acess",
            },
            status=HTTP_406_NOT_ACCEPTABLE,
        )


class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class AuthorCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorSerializer


class AuthorDetail(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


def home(request):
    return HttpResponse('hi')


def export_data(request, genre):
    if request.user.is_staff:
        if (genre and genre != 'all'):
            book_query = Book.objects.filter(genre__name__contains=genre)
        else:
            book_query = Book.objects.all()

        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": 'attachment; filename="somefilename.csv"'},
        )

        writer = csv.writer(response)
        for i in book_query:
            author_list = ""
            for j in i.authors.all():

                author_list += j.username if j.username != None else ""
                writer.writerow([i.name, i.genre.name, i.pages,
                                 i.cover_image, author_list])

        return response

    return JsonResponse({'message': 'Invalid acess'})
