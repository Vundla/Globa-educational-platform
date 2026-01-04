"""
Apache Signal Handlers for Educational Platform Models
This module implements Django signal handlers that work with Apache/WSGI
to ensure proper signal handling for all model lifecycle events.
"""

import logging
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Course, Lesson, Enrollment, Assignment, Submission

# Configure logging for Apache signal handling
logger = logging.getLogger(__name__)


# Course Signals
@receiver(pre_save, sender=Course)
def course_pre_save(sender, instance, **kwargs):
    """Handle pre-save signal for Course model with Apache compatibility"""
    logger.info(f"Apache Signal: Course pre_save - {instance.title}")
    # Add any pre-save logic here


@receiver(post_save, sender=Course)
def course_post_save(sender, instance, created, **kwargs):
    """Handle post-save signal for Course model with Apache compatibility"""
    action = "created" if created else "updated"
    logger.info(f"Apache Signal: Course post_save - {instance.title} ({action})")
    # Add any post-save logic here


@receiver(pre_delete, sender=Course)
def course_pre_delete(sender, instance, **kwargs):
    """Handle pre-delete signal for Course model with Apache compatibility"""
    logger.info(f"Apache Signal: Course pre_delete - {instance.title}")
    # Add any pre-delete logic here


@receiver(post_delete, sender=Course)
def course_post_delete(sender, instance, **kwargs):
    """Handle post-delete signal for Course model with Apache compatibility"""
    logger.info(f"Apache Signal: Course post_delete - {instance.title}")
    # Add any post-delete logic here


# Lesson Signals
@receiver(pre_save, sender=Lesson)
def lesson_pre_save(sender, instance, **kwargs):
    """Handle pre-save signal for Lesson model with Apache compatibility"""
    logger.info(f"Apache Signal: Lesson pre_save - {instance.title}")


@receiver(post_save, sender=Lesson)
def lesson_post_save(sender, instance, created, **kwargs):
    """Handle post-save signal for Lesson model with Apache compatibility"""
    action = "created" if created else "updated"
    logger.info(f"Apache Signal: Lesson post_save - {instance.title} ({action})")


@receiver(pre_delete, sender=Lesson)
def lesson_pre_delete(sender, instance, **kwargs):
    """Handle pre-delete signal for Lesson model with Apache compatibility"""
    logger.info(f"Apache Signal: Lesson pre_delete - {instance.title}")


@receiver(post_delete, sender=Lesson)
def lesson_post_delete(sender, instance, **kwargs):
    """Handle post-delete signal for Lesson model with Apache compatibility"""
    logger.info(f"Apache Signal: Lesson post_delete - {instance.title}")


# Enrollment Signals
@receiver(pre_save, sender=Enrollment)
def enrollment_pre_save(sender, instance, **kwargs):
    """Handle pre-save signal for Enrollment model with Apache compatibility"""
    logger.info(f"Apache Signal: Enrollment pre_save - {instance.student.username} in {instance.course.title}")


@receiver(post_save, sender=Enrollment)
def enrollment_post_save(sender, instance, created, **kwargs):
    """Handle post-save signal for Enrollment model with Apache compatibility"""
    action = "created" if created else "updated"
    logger.info(f"Apache Signal: Enrollment post_save - {instance.student.username} in {instance.course.title} ({action})")


@receiver(pre_delete, sender=Enrollment)
def enrollment_pre_delete(sender, instance, **kwargs):
    """Handle pre-delete signal for Enrollment model with Apache compatibility"""
    logger.info(f"Apache Signal: Enrollment pre_delete - {instance.student.username} from {instance.course.title}")


@receiver(post_delete, sender=Enrollment)
def enrollment_post_delete(sender, instance, **kwargs):
    """Handle post-delete signal for Enrollment model with Apache compatibility"""
    logger.info(f"Apache Signal: Enrollment post_delete - {instance.student.username} from {instance.course.title}")


# Assignment Signals
@receiver(pre_save, sender=Assignment)
def assignment_pre_save(sender, instance, **kwargs):
    """Handle pre-save signal for Assignment model with Apache compatibility"""
    logger.info(f"Apache Signal: Assignment pre_save - {instance.title}")


@receiver(post_save, sender=Assignment)
def assignment_post_save(sender, instance, created, **kwargs):
    """Handle post-save signal for Assignment model with Apache compatibility"""
    action = "created" if created else "updated"
    logger.info(f"Apache Signal: Assignment post_save - {instance.title} ({action})")


@receiver(pre_delete, sender=Assignment)
def assignment_pre_delete(sender, instance, **kwargs):
    """Handle pre-delete signal for Assignment model with Apache compatibility"""
    logger.info(f"Apache Signal: Assignment pre_delete - {instance.title}")


@receiver(post_delete, sender=Assignment)
def assignment_post_delete(sender, instance, **kwargs):
    """Handle post-delete signal for Assignment model with Apache compatibility"""
    logger.info(f"Apache Signal: Assignment post_delete - {instance.title}")


# Submission Signals
@receiver(pre_save, sender=Submission)
def submission_pre_save(sender, instance, **kwargs):
    """Handle pre-save signal for Submission model with Apache compatibility"""
    logger.info(f"Apache Signal: Submission pre_save - {instance.student.username} for {instance.assignment.title}")


@receiver(post_save, sender=Submission)
def submission_post_save(sender, instance, created, **kwargs):
    """Handle post-save signal for Submission model with Apache compatibility"""
    action = "created" if created else "updated"
    logger.info(f"Apache Signal: Submission post_save - {instance.student.username} for {instance.assignment.title} ({action})")


@receiver(pre_delete, sender=Submission)
def submission_pre_delete(sender, instance, **kwargs):
    """Handle pre-delete signal for Submission model with Apache compatibility"""
    logger.info(f"Apache Signal: Submission pre_delete - {instance.student.username} for {instance.assignment.title}")


@receiver(post_delete, sender=Submission)
def submission_post_delete(sender, instance, **kwargs):
    """Handle post-delete signal for Submission model with Apache compatibility"""
    logger.info(f"Apache Signal: Submission post_delete - {instance.student.username} for {instance.assignment.title}")
