from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view()
def gethome(request):
    return Response({
        'status': 200,
        'message': 'Yes , Django rest framework is working'
    })
