from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from . import serializers
from . import models

# Create your views here.

class WineApiView(APIView):

    serializer_class = serializers.WineSerializer

    def get(self, request, format=None):

        return Response({'message' : 'Hello'})

    
    def post(self, request):

        serializer = serializers.WineSerializer(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            message = 'Description: {0}'.format(description)

            return Response({'message' : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):

        return Response({'method': 'put'})

    def patch(self, request, pk=None):

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):

        return Response({'method': 'delete'})
    

class WineViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.WineSerializer
    queryset = models.WineDetail.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('country', 'province', 'variety', 'winery',)