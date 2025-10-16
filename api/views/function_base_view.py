from django.shortcuts import render
from students.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employees.models import Employee
from api.serializers import EmployeeSerializer


# Create your views here.
#Student CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentView(request):
    if(request.method == 'GET'):
        # Get all the data from the Student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(students, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method == 'POST'):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Employee CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employeeView(request):
    if(request.method == 'GET'):
        # Get all the data from the Employee table
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        print(employees, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method == 'POST'):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def employee(request, emp_id):
    try:
        employee = Employee.objects.get(pk=emp_id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)