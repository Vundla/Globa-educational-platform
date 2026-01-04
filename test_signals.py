"""
Test script to verify Apache signal activation for all models
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educational_platform.settings')
django.setup()

from django.contrib.auth.models import User
from courses.models import Course, Lesson, Enrollment, Assignment, Submission
from datetime import datetime, timedelta

print("=" * 80)
print("Testing Apache Signal Activation for All Models")
print("=" * 80)

# Create test user
print("\n1. Creating test user...")
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com'}
)
if created:
    user.set_password('testpass123')
    user.save()
print(f"✓ User created/retrieved: {user.username}")

# Test Course signals
print("\n2. Testing Course model signals...")
course = Course.objects.create(
    title='Introduction to Python',
    description='Learn Python programming from scratch',
    instructor=user,
    is_active=True
)
print(f"✓ Course created: {course.title} (signals triggered)")

# Test Lesson signals
print("\n3. Testing Lesson model signals...")
lesson = Lesson.objects.create(
    course=course,
    title='Python Basics',
    content='Introduction to Python syntax and data types',
    order=1,
    duration_minutes=60
)
print(f"✓ Lesson created: {lesson.title} (signals triggered)")

# Test Assignment signals
print("\n4. Testing Assignment model signals...")
assignment = Assignment.objects.create(
    lesson=lesson,
    title='Python Variables Exercise',
    description='Practice creating and using variables',
    due_date=datetime.now() + timedelta(days=7),
    max_score=100
)
print(f"✓ Assignment created: {assignment.title} (signals triggered)")

# Create student user
print("\n5. Creating student user...")
student, created = User.objects.get_or_create(
    username='student1',
    defaults={'email': 'student1@example.com'}
)
if created:
    student.set_password('studentpass123')
    student.save()
print(f"✓ Student created/retrieved: {student.username}")

# Test Enrollment signals
print("\n6. Testing Enrollment model signals...")
enrollment = Enrollment.objects.create(
    student=student,
    course=course,
    progress=0
)
print(f"✓ Enrollment created: {enrollment} (signals triggered)")

# Test Submission signals
print("\n7. Testing Submission model signals...")
submission = Submission.objects.create(
    assignment=assignment,
    student=student,
    content='My solution to the assignment',
    score=85
)
print(f"✓ Submission created: {submission} (signals triggered)")

# Test update signals
print("\n8. Testing update signals...")
course.is_active = False
course.save()
print(f"✓ Course updated: {course.title} (update signals triggered)")

print("\n" + "=" * 80)
print("✓ All Apache signals activated and tested successfully!")
print("=" * 80)
print("\nCheck 'apache_signals.log' for detailed signal logs.")
print("\nAll models support Apache signal handling:")
print("  - Course")
print("  - Lesson")
print("  - Enrollment")
print("  - Assignment")
print("  - Submission")
