#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = BASE_DIR + '/.env'

print(ENV_FILE)

if (not os.path.isfile(ENV_FILE)):
  os.popen(f'cd {BASE_DIR} && cp .env.example .env')

load_dotenv(dotenv_path=ENV_FILE)


def main():
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
  try:
    from django.core.management import execute_from_command_line
  except ImportError as exc:
    raise ImportError(
      "Couldn't import Django. Are you sure it's installed and "
      "available on your PYTHONPATH environment variable? Did you "
      "forget to activate a virtual environment?") from exc
  execute_from_command_line(sys.argv)


if __name__ == '__main__':
  main()
