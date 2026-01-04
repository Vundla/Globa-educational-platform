from django.contrib import admin
from .models import Course, Lesson, Enrollment, Assignment, Submission


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Course admin with Apache signal support"""
    list_display = ['title', 'instructor', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Lesson admin with Apache signal support"""
    list_display = ['title', 'course', 'order', 'duration_minutes', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'content']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    """Enrollment admin with Apache signal support"""
    list_display = ['student', 'course', 'enrolled_at', 'completed', 'progress']
    list_filter = ['completed', 'enrolled_at']
    search_fields = ['student__username', 'course__title']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    """Assignment admin with Apache signal support"""
    list_display = ['title', 'lesson', 'due_date', 'max_score', 'created_at']
    list_filter = ['due_date', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """Submission admin with Apache signal support"""
    list_display = ['student', 'assignment', 'submitted_at', 'score']
    list_filter = ['submitted_at', 'score']
    search_fields = ['student__username', 'assignment__title']

