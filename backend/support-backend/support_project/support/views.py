from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import TicketSerializer, AgentSerializer
from .models import Ticket, Agent

# Create your views here.
MASTERKEY = 'password'

@api_view(['GET', 'POST'])
def TicketView(request):

    # check if key = MASTERKEY
    if KeyCheck(key) == False :
        messages = {
            "msg" : "Key Invalid"
        }
        return Response(messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def TicketDetailsView(request, pk, key):

    # check if key = MASTERKEY
    if KeyCheck(key) == False :
        messages = {
            "msg" : "Key Invalid"
        }
        return Response(messages, status=status.HTTP_400_BAD_REQUEST)

    try:
        query = Ticket.objects.get(pk=pk)
    except query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TicketSerializer(query)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def AgentView(request):
# check if key = MASTERKEY
    if KeyCheck(key) == False :
        messages = {
            "msg" : "Key Invalid"
        }
        return Response(messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        queryset = Agent.objects.all()
        serializer = AgentSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def AgentDetailsView(request, pk):
# check if key = MASTERKEY
    if KeyCheck(key) == False :
        messages = {
            "msg" : "Key Invalid"
        }
        return Response(messages, status=status.HTTP_400_BAD_REQUEST)

    try:
        query = Agent.objects.get(pk=pk)
    except query.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgentSerializer(query)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

def KeyCheck(key):
    if key == MASTERKEY :
        return True
    else : 
        return False

    