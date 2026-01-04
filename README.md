# Globa Educational Platform

A Django-based educational platform with **Apache signal activation for all models**.

## Features

- **Apache Signal Support**: All models (Course, Lesson, Enrollment, Assignment, Submission) have Apache/WSGI signal handlers
- **Model Lifecycle Signals**: Pre-save, post-save, pre-delete, and post-delete signals for all models
- **WSGI Signal Handling**: Proper Apache signal handling (SIGUSR1, SIGTERM, SIGHUP)
- **Comprehensive Logging**: All signal events are logged for debugging and monitoring
- **Educational Platform**: Complete course management system

## Models with Apache Signal Support

1. **Course** - Educational courses with instructor management
2. **Lesson** - Course lessons with ordering and duration
3. **Enrollment** - Student course enrollments with progress tracking
4. **Assignment** - Lesson assignments with due dates
5. **Submission** - Student assignment submissions with scoring

## Setup Instructions

### Prerequisites

- Python 3.8+
- Apache with mod_wsgi (for production)
- Django 4.2+

### Installation

```bash
# Clone the repository
git clone https://github.com/Vundla/Globa-educational-platform.git
cd Globa-educational-platform

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Apache Deployment

1. Copy `apache_config.conf` to your Apache sites-available directory
2. Update paths in the configuration file
3. Enable the site: `sudo a2ensite educational_platform`
4. Reload Apache: `sudo systemctl reload apache2`

## Apache Signal Commands

- **Graceful Restart**: `apachectl graceful` (sends SIGUSR1)
- **Stop**: `apachectl stop` (sends SIGTERM)
- **Restart**: `apachectl restart` (sends SIGHUP)

## Signal Logging

All model signals are logged to:
- Console output
- `apache_signals.log` file

## Theia IDE Support

This project is fully compatible with Eclipse Theia IDE. All Apache signals work seamlessly in Theia-based development environments.

## Development

Access the admin panel at `http://localhost:8000/admin/` to manage:
- Courses
- Lessons
- Enrollments
- Assignments
- Submissions

All CRUD operations will trigger appropriate Apache signals that are logged for monitoring.

## License

MIT License - See LICENSE file for details
