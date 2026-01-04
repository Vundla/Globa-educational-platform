# Theia IDE Configuration for Educational Platform

This document provides instructions for using the Educational Platform with Apache signals in Theia IDE.

## Overview

The Educational Platform is fully compatible with Eclipse Theia IDE and includes Apache signal handling for all models. All Django model signals (pre_save, post_save, pre_delete, post_delete) are activated and logged.

## Quick Start in Theia IDE

### 1. Open Project in Theia

```bash
# The project is already cloned
cd /home/runner/work/Globa-educational-platform/Globa-educational-platform
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize Database

```bash
# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### 4. Test Apache Signal Activation

```bash
# Run the signal test script
python test_signals.py
```

This will create test data and trigger all Apache signals for all models. Check the output and `apache_signals.log` file.

### 5. Run Development Server

```bash
python manage.py runserver
```

## Apache Signal Features

### Supported Models
All models have Apache signal handlers:
- **Course**: Educational courses
- **Lesson**: Course lessons
- **Enrollment**: Student enrollments
- **Assignment**: Lesson assignments
- **Submission**: Assignment submissions

### Signal Types
Each model supports:
- `pre_save`: Before saving to database
- `post_save`: After saving to database
- `pre_delete`: Before deleting from database
- `post_delete`: After deleting from database

### Signal Logging
All signals are logged to:
- **Console**: Visible in terminal output
- **File**: `apache_signals.log` in project root

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/` to:
- Create and manage courses
- Add lessons to courses
- Manage student enrollments
- Create assignments
- Review submissions

All CRUD operations will trigger appropriate Apache signals.

## Testing Signals in Theia

### Using Python Shell

```bash
python manage.py shell
```

Then test signals:

```python
from django.contrib.auth.models import User
from courses.models import Course

# Create a user
user = User.objects.create_user('testuser', 'test@example.com', 'password')

# Create a course (triggers pre_save and post_save signals)
course = Course.objects.create(
    title='Test Course',
    description='Testing signals',
    instructor=user
)

# Update course (triggers pre_save and post_save signals)
course.title = 'Updated Course'
course.save()

# Delete course (triggers pre_delete and post_delete signals)
course.delete()
```

### Monitoring Signal Logs

In Theia terminal:

```bash
# Watch log file in real-time
tail -f apache_signals.log
```

## Apache Deployment from Theia

When ready to deploy with Apache:

1. Copy `apache_config.conf` to Apache configuration
2. Update paths in configuration file
3. Install mod_wsgi: `pip install mod_wsgi`
4. Configure Apache to use the WSGI file

## Troubleshooting

### Signals Not Firing
- Ensure app is in INSTALLED_APPS (settings.py)
- Check that signals.py is imported in apps.py ready() method
- Verify logging configuration in settings.py

### Import Errors
- Ensure virtual environment is activated
- Install all requirements: `pip install -r requirements.txt`

### Database Issues
- Run migrations: `python manage.py migrate`
- Delete db.sqlite3 and re-run migrations if needed

## Development Workflow in Theia

1. Make model changes in `courses/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Update signals in `courses/signals.py` if needed
5. Test changes: `python test_signals.py`
6. Check logs: `cat apache_signals.log`

## Additional Resources

- Django Signals Documentation: https://docs.djangoproject.com/en/stable/topics/signals/
- Apache mod_wsgi: https://modwsgi.readthedocs.io/
- Eclipse Theia: https://theia-ide.org/

## Support

For issues or questions, refer to the main README.md file or project documentation.
