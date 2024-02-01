from rest_framework.serializers import ModelSerializer


from . models import Genre, Book, Author


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id','auth_id','books','username','password','phone','city','profile_image']

