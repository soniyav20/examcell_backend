from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Complaint, Department
from .serializers import ComplaintSerializer, DepartmentSerializer


class ComplaintsByDepartmentView(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    def get_queryset(self):
        dept_name = self.kwargs['dept_name']
        department = Department.objects.get(name=dept_name)
        return Complaint.objects.filter(dept_id=department)


class ComplaintsView(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    def get_queryset(self):
        return Complaint.objects.all()

class ComplaintsViewbyStudent(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Complaint.objects.filter(student_id=student_id)


class DepartmentView(generics.ListAPIView):
    queryset= Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ComplaintsCreate(generics.CreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class ComplaintsDelete(generics.DestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    lookup_field = 'complaint_id'

class DepartmentDelete(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'dept_id'

class ComplaintStatusUpdate(generics.UpdateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    lookup_field = 'complaint_id'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        status_value = request.data.get('status')  # Assuming 'status' is the field to be updated
        if status_value is not None:
            instance.status = status_value
            instance.save()
            return Response({'message': 'Status updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Status field is required'}, status=status.HTTP_400_BAD_REQUEST)

class DepartmentUpdate(generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_url_kwarg = 'dept_id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class UpdateComplaintsByDepartment(generics.UpdateAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        dept = self.kwargs['dept_id']
        return Complaint.objects.filter(dept_id=dept)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, data=request.data, partial=partial, many=True)
        serializer.is_valid(raise_exception=True)
        updated_complaints = serializer.save()
        return Response(self.get_serializer(updated_complaints, many=True).data)
    lookup_field = 'dept_id'

class ComplaintUpdateByDepartment(generics.UpdateAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        dept_name = self.kwargs['dept_name']
        department = Department.objects.get(name=dept_name)
        return Complaint.objects.filter(dept_id=department)

    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = request.data
        for complaint in queryset:
            serializer = self.get_serializer(complaint, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
        return Response({'message': 'Complaints updated successfully'}, status=status.HTTP_200_OK)
