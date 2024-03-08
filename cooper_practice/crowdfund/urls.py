from django.urls import path

from .views import (
    ComplaintsByDepartmentView,
    ComplaintsViewbyStudent,
    ComplaintsCreate,
    DepartmentCreate,
    ComplaintsDelete,
    DepartmentDelete,
    ComplaintStatusUpdate,
    DepartmentUpdate,
    DepartmentView,
    UpdateComplaintsByDepartment,
    ComplaintsView
)

urlpatterns = [

    path('complaints/department/<str:dept_name>/', ComplaintsByDepartmentView.as_view(), name='complaints_by_department'),
    path('getdepartments/', DepartmentView.as_view(), name='department_view'),
    path('getcomplaints/', ComplaintsView.as_view()),
    path('getcomplaints/student/<int:student_id>/', ComplaintsViewbyStudent.as_view()),

    path('complaints/create/', ComplaintsCreate.as_view(), name='create_complaint'),
    path('department/create/', DepartmentCreate.as_view(), name='create_department'),

    path('complaints/deletec/<int:complaint_id>/', ComplaintsDelete.as_view(), name='delete_complaint'),
    path('department/delete/<int:dept_id>/', DepartmentDelete.as_view(), name='delete_department'),

    path('complaints/update/<int:complaint_id>/', ComplaintStatusUpdate.as_view(), name='update_complaint_status'),
    path('department/update/<int:dept_id>/', DepartmentUpdate.as_view(), name='update_department'),

    path('complaints/department/update/<int:dept_id>/', UpdateComplaintsByDepartment.as_view(), name='update_complaints_by_department'),
]
