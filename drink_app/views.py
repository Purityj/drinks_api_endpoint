from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# all endpoints are created in views.py. 
# Endpoint is a url you can access data from
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize them using the DrinkSerializer class. many=True will serialize all the drinks in the list
        serializer = DrinkSerializer(drinks, many=True)
        # return json response
        # return JsonResponse({"drinks": serializer.data})
        return Response(serializer.data)     #returns all data in a cool DRF HTMLL UI 
    
    if request.method == 'POST':
        # add a drink to the database
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])  
def drink_detail(request, id, format=None):
    # check request to ensure its valid
    try:
       drink = Drink.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


