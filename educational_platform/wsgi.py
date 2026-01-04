"""
Apache WSGI configuration for educational_platform project.

This file contains the WSGI application used by Apache and other WSGI servers
to serve the educational platform with proper signal handling.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
import signal

from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educational_platform.settings')

# Add project directory to Python path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

# Get the WSGI application
application = get_wsgi_application()

# Apache Signal Handling for graceful reloads and shutdowns
def handle_sigusr1(signum, frame):
    """Handle SIGUSR1 signal from Apache for graceful restart"""
    print("Apache Signal: Received SIGUSR1 - Graceful restart initiated")

def handle_sigterm(signum, frame):
    """Handle SIGTERM signal from Apache for shutdown"""
    print("Apache Signal: Received SIGTERM - Shutdown initiated")

def handle_sighup(signum, frame):
    """Handle SIGHUP signal from Apache for configuration reload"""
    print("Apache Signal: Received SIGHUP - Configuration reload initiated")

# Register Apache signal handlers
signal.signal(signal.SIGUSR1, handle_sigusr1)
signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGHUP, handle_sighup)

print("Apache Signal Handlers Activated for Educational Platform")

