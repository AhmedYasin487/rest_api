from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profile_api import serializers

from rest_framework import viewsets

class HelloWorldApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'This is is is sis si sis sis s ',
            'This is is is sis si sis sis s ',
            'This is is is sis si sis sis s ',
            'This is is is sis si sis sis s ',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})

        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
# Create your views here.
# class HelloViewSet(viewsets.ViewSet):
     
class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self,request):

        a_viewset = [
            'This is is is sis si sis sis s ',
            'This is is is sis si sis sis s ',
            'This is is is sis si sis sis s ',
            'This is is is sis si sis sis s ',
        ]

        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}!'
            return Response({'message':message})

        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'Patch'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})
