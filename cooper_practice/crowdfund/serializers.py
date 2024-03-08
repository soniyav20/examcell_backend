from dataclasses import field
from rest_framework import serializers
from .models import Complaint, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields='__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields='__all__'
