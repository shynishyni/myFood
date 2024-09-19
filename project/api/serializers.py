from rest_framework import serializers
from .models import FoodDetails
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDetails
        fields = '__all__'