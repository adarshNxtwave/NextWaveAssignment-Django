import datetime
from ecommerceDb2.models import Student,Professor,Course,Enrollment
from django.db.models import Count

# Task 1: Get Student Details
# SQL Query:
# SELECT * FROM Student WHERE name IN ('Alice', 'Bob');

def get_students_by_given_names(student_names):
    student_details = Student.objects.filter(name__in = student_names)
    return list(student_details.values())


# Task 2: Get Courses Taught by a Specific Professor
# SQL Query:
# SELECT * FROM Course WHERE professor_id = (SELECT professor_id FROM Professor WHERE name = 'Dr. Smith');

def get_courses_by_professor(professor_name):
    if not professor_name:
        professor_name = 'Dr. Smith'

    courses = Course.objects.get(professor__name = professor_name)
    return list(courses.values())


# Task 3: Get Students Enrolled in a Specific Course
# SQL Query:
# SELECT s.name FROM Student s
# JOIN Enrollment e ON s.student_id = e.student_id
# JOIN Course c ON e.course_id = c.course_id
# WHERE c.name = 'Mathematics';

def get_students_in_course(course_name):
    if not course_name:
        course_name = 'Mathematics'

    """
    :return: List of student names.
    """
    course_names = Enrollment.objects.filter(course__name = course_name) # to check can i use student__name for select related
    return list(course_names.values_list('student__name',flat = True))



# Task 4: Get Courses with More than 5 Students Enrolled
# SQL Query:
# SELECT course_id FROM Enrollment GROUP BY course_id HAVING COUNT(*) > 5;
# Django ORM:
def get_popular_courses():

    return list(Course.objects.annotate(count=Count('enrollments')).filter(count__gt=5))

    """
    :return: List of course names.
    """


# Task 5: Get Students Who Received an 'A' Grade
# SQL Query:
# SELECT DISTINCT s.name FROM Student s
# JOIN Enrollment e ON s.student_id = e.student_id
# WHERE e.grade = 'A';

def get_students_with_A_grade():
    return list(Enrollment.objects.filter(grade = 'A').values_list('student',flat = True ).distinct())
    """
    :return: List of student names.
    """


# Task 6: Get Professors Teaching More Than Two Courses
# SQL Query:
# SELECT professor_id FROM Course GROUP BY professor_id HAVING COUNT(*) > 2;

def get_professors_with_multiple_courses():
    return list(Professor.objects.annotate(count=Count('courses')).filter(count__gt=2).distinct())
    """
    :return: List of professor names.
    """


# Task 7: Get Courses With No Enrollments
# SQL Query:
# SELECT c.name FROM Course c LEFT JOIN Enrollment e ON c.course_id = e.course_id WHERE e.enrollment_id IS NULL;

def get_courses_with_no_enrollments():
    """
    :return: List of course names.
    """
    return list(Course.objects.filter(enrollments__isnull=True).values_list('name',flat = True))


# Task 8: Get Students Enrolled in at Least Three Courses
# SQL Query:
# SELECT student_id FROM Enrollment GROUP BY student_id HAVING COUNT(*) >= 3;

def get_students_with_multiple_enrollments():
    return list(Student.objects.annotate(count=Count('enrollments')).filter(count__gte=2).values_list('student_id',flat = True))
    """
    :return: List of student names.
    """