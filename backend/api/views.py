from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

class StudentApi (APIView) :
    def get(self, request) :
        queryset = Student.objects.all()
        serializers = StudentSerializers (queryset, many = True)

        return Response ({
            'status' : True,
            'data' : serializers.data
        })
    
    # step 4