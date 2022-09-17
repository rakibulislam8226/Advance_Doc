from rest_framework import serializers
from .models import City, Country


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