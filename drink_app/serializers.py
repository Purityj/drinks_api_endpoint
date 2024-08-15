from rest_framework import serializers
from .models import Drink

# describes the process of changing data from python object to json
# we will use this serializer when returning our model through the API 
class DrinkSerializer(serializers.ModelSerializer):
    # metadata describing our Drink model
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']


