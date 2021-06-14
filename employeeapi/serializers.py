# api <-> mobile app / web app / etc . json
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' # ('id', 'fullname') if you want to add only few columns
