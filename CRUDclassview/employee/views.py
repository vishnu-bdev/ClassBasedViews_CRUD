from django.shortcuts import render

# Create your views here.
from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeView(APIView):

    def get(self, request):
        emp = Employee.objects.all()
        emp_serializer = EmployeeSerializer(emp, many=True)
        return Response(emp_serializer.data)

    def post(self, request):
        emp_data = EmployeeSerializer(data = request.data)
        if emp_data.is_valid():
            emp_data.save()
            return Response(emp_data.data, status=status.HTTP_201_CREATED)
        return Response(emp_data.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeUpdateview(APIView):
    
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        emp_obj = self.get_object(pk)
        serializer = EmployeeSerializer(emp_obj)
        return Response(serializer.data)


    def put(self, request, pk):
        emp_obj = self.get_object(pk)
        serializer = EmployeeSerializer(emp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        emp_obj = self.get_object(pk)
        emp_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


