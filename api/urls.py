from django.urls import path
from api.views import function_base_view
from  api.views import class_base_view

urlpatterns = [
    path('fbv-students/', function_base_view.studentView),
    path('fbv-students/<int:student_id>/', function_base_view.student),
    path('fbv-employees/', function_base_view.employeeView),
    path('fbv-employees/<int:emp_id>/', function_base_view.employee),

    path('fbv-student/', class_base_view.StudentView.as_view())
]