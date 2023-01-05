from rest_framework import serializers
from model_abstraction import models


# StudentGUB
class StudentGUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentGUB
        fields = "__all__"
 
# StudentDIU        
class StudentDIUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentDIU
        fields = "__all__"
        
# BookABS        
class AbsBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
        
        
# ISBN        
class ISBNSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ISBN
        fields = "__all__"
        
# Person        
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"