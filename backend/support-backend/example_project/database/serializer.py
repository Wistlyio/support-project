from rest_framework import serializers
from .models import Student 


class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student 
        fields = ('id', 'first_name', 'last_name', 'gender', 'age',
        'date_created', 'email')
        read_only_fields = ['id']