# Generated by Django 4.2.11 on 2024-03-06 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('head_of_dept', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('complaint_text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='pending', max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdfund.department')),
            ],
        ),
    ]
