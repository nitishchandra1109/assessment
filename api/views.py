from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import  EmployeeSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

@api_view(['GET'])
def employee_list(request):
    query_set = Employee.objects.all()
    serializer = EmployeeSerializers(query_set,many=True)
    return Response(serializer.data)



class EventNewsItems(APIView, LimitOffsetPagination):
    def get(self, request, format=None):
        query_set = Employee.objects.all()
        results = self.paginate_queryset(query_set, request, view=self)
        serializer = EmployeeSerializers(results, many=True)
        return self.get_paginated_response(serializer.data)