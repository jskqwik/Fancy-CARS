from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["vin","make","model","engine","interior_color","body_color","year","image","image_url","speed"]