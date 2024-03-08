from django.db import models

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    complaint_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    complaint_text = models.TextField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to='complaint_photos/', null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    student_id = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Complaint #{self.complaint_id} - {self.location} ({self.status})"
