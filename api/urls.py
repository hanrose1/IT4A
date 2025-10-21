from django.urls import path
from api.views import employee_function_base_view
from api.views import student_function_base_view
from  api.views import student_class_base_view
from  api.views import employee_class_base_view

urlpatterns = [
    path('fbv-students/', student_function_base_view.studentView),
    path('fbv-students/<int:student_id>/', student_function_base_view.student),
    path('fbv-employees/', employee_function_base_view.employeeView),
    path('fbv-employees/<int:emp_id>/', employee_function_base_view.employee),

    path('cbv-students/', student_class_base_view.StudentView.as_view()),
    path('cbv-students/<int:pk>/', student_class_base_view.StudentDetail.as_view()),
    path('cbv-employees/', employee_class_base_view.EmployeeView.as_view()),
    path('cbv-employees/<int:pk>/', employee_class_base_view.EmployeeDetail.as_view())
]