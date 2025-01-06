from rest_framework import serializers
from .models import *

class Emp(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'