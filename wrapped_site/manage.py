#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Sets default Django settings module to settings.py"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wrapped_site.settings')
    """Import the function that handles executing management commands like makemigrate"""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    """Now actually call the function that executes the management commands"""
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
