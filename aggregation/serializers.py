from rest_framework import serializers
from aggregation.models import Author, Publisher, Book, Store


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

