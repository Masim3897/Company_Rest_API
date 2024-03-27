from django.shortcuts import render
from rest_framework import viewsets
from API.models import company,Employee
from API.serializers import companyserializer,Employeeserializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companyserializer
    
    #/companies/{id}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        cmpany= company.objects.get(pk=pk)
        emps = Employee.objects.filter(cmpany=cmpany)
        emps_serializer = Employeeserializer(emps,many = True, 
                                             context = {'request':request})
        return Response(emps_serializer.data)
    
    
    
    
    
    
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer    
    
