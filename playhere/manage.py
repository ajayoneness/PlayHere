#!/usr/bin/env python

#https://www.canva.com/design/DAFRWsFKEmQ/1A9mj__1CsfNyglXoT2hew/view?utm_content=DAFRWsFKEmQ&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent
#https://www.canva.com/design/DAFR5SnoNbE/0AfHCQHaqAwQlXvLfbV__g/edit?utm_content=DAFR5SnoNbE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

"""Django's command-line utility for administrative tasks."""
import os
import sys
os.environ["PATH"] += os.pathsep + "/usr/bin/dot"


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'playhere.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
