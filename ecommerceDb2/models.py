from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

class Professor(models.Model):
    professor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='courses')
    credits = models.PositiveIntegerField()

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    grade = models.CharField(max_length=2)