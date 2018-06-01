from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer


# Create your views here.

#List all stocks or create a newone

class StockList(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StockSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        