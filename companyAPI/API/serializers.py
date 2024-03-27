from rest_framework import serializers
from API.models import company,Employee

class companyserializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = company
        fields = "__all__"
        
class Employeeserializer(serializers.HyperlinkedModelSerializer):
    employee__id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"        
