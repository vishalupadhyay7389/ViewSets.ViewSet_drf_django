from django.shortcuts import render
from .models import Employee , EmployeeSerlizer
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.
class EmployeeDeatilView(ViewSet):
    def list(self , request):
        empl = Employee.objects.all()
        emplser = EmployeeSerlizer(empl , many=True)
        return Response(emplser.data)
    
    def retrieve(self , request , pk=None):
        try:
            empl = Employee.objects.get(pk = pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        emplser = EmployeeSerlizer(empl)
        return Response(emplser.data)
            
