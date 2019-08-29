# from rest_framework import serializers
# from .models import Student 


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Student 
#         fields = ('id', 'first_name', 'last_name', 'gender', 'age',
#         'date_created', 'email')
#         read_only_fields = ['id']

from rest_framework import serializers
from .models import Ticket
from .models import Agent

class TicketSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Ticket
        fields = ('id', 'first_name', 'last_name', 'date_created', 'email',
        'issue_summary', 'extra_details' )
        read_only_fields = ['id']

class AgentSerializer(serializers.ModelSerializer) :
    class Meta: 
        model = Agent
        fields = ('id', 'first_name', 'last_name', 'email')
        read_only_fields = ['id']