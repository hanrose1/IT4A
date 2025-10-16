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
    
    #Ga create ug employee
    if(request.method == 'POST'):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
#emp_id(parameter->urls.py)
def employee(request, emp_id):
    #Try Fetching Employee object according to its requested id(Employee obj kay naa sa employee model???)
    try:
        employee = Employee.objects.get(pk=emp_id)
        #If no employee exist it return a response 404
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    #If employee exist, request method to get the employee
    if request.method == 'GET':
        #Since employee is an object, serializer converts the data into JSON
        serializer = EmployeeSerializer(employee)
        #Then it returns converted employeed data with a status 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)
    #Else if mag update, request method/trigger an action PUT
    elif request.method == 'PUT':
        #Then kaning request.data is from client. Since si client nagupdate. Iagi ug serializer.
        serializer = EmployeeSerializer(employee, data=request.data)
        #I-check dayun kung ang serializer in which is ang sulod kay employee object, ug ang request data ni client is valid. 
        if serializer.is_valid():
            #Kung valid -> gi save
            serializer.save()
            #Mu return dayon sya ug updated employee with status nga 200 OK
            return Response(serializer.data, status=status.HTTP_200_OK)
        #kung dile VALID -> mu return ug badrequest and error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Else if kung idelete nimo, request sya ug method delete
    elif request.method == 'DELETE':
        #then kaning si employee, makita nato sa try: employee with emp_id. Specific employee na ni. Delete.
        employee.delete()
        #Then return dayon sya ug 204 no content kay wa namay content
        return Response(status=status.HTTP_204_NO_CONTENT)