from django.shortcuts import render
from rest_framework.response import Response
from . serializers import employeesSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from . models import employees
from rest_framework.views import APIView

# Create your views here.

class employeesList(APIView):
    def get(self, request):
        employees1= employees.objects.all()
        serializer= employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
    
