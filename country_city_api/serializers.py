from rest_framework import serializers
from .models import City, Country, StudentList


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        
class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True, many=False)
    class Meta:
        model = City
        fields = '__all__'
        extra_fields = ['country']
        

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentList
        fields = ["id","name", "roll","city","passby",]