from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Complaint, Department
from .serializers import ComplaintSerializer, DepartmentSerializer

# View complaints by department
@api_view(['GET'])
def complaints_by_department(request, dept_name):
    department = get_object_or_404(Department, name=dept_name)
    complaints = Complaint.objects.filter(dept_id=department)
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)

# View all complaints
@api_view(['GET'])
def complaints_list(request):
    complaints = Complaint.objects.all()
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)

# View complaints by a specific student
@api_view(['GET'])
def complaints_by_student(request, student_id):
    complaints = Complaint.objects.filter(student_id=student_id)
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)

# List all departments
@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)

# Create a new department
@api_view(['POST'])
def department_create(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create a new complaint
@api_view(['POST'])
def complaint_create(request):
    serializer = ComplaintSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a complaint
@api_view(['DELETE'])
def complaint_delete(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
    complaint.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Delete a department
@api_view(['DELETE'])
def department_delete(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    department.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Update complaint status
@api_view(['PUT'])
def complaint_status_update(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
    status_value = request.data.get('status')
    if status_value is not None:
        complaint.status = status_value
        complaint.save()
        return Response({'message': 'Status updated successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Status field is required'}, status=status.HTTP_400_BAD_REQUEST)

# Update department
@api_view(['PUT', 'PATCH'])
def department_update(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    serializer = DepartmentSerializer(department, data=request.data, partial=request.method == 'PATCH')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update complaints by department
@api_view(['PUT'])
def update_complaints_by_department(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    complaints = Complaint.objects.filter(dept_id=department)
    serializer = ComplaintSerializer(complaints, data=request.data, many=True, partial=True)
    if serializer.is_valid():
        updated_complaints = serializer.save()
        return Response(ComplaintSerializer(updated_complaints, many=True).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update complaints by department name
@api_view(['PUT'])
def complaint_update_by_department(request, dept_name):
    department = get_object_or_404(Department, name=dept_name)
    complaints = Complaint.objects.filter(dept_id=department)
    for complaint in complaints:
        serializer = ComplaintSerializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
    return Response({'message': 'Complaints updated successfully'}, status=status.HTTP_200_OK)
