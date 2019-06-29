# Django React Boilerplate

A Django boilerplate with React and Webpack.

## Installation

1. Frontend
   - `cd frontend`
   - `npm i`
   - `npm run hot`
2. Backend
   - `cd backend`
   - `pip install -r requirements.txt`
   - `cp .env.example .env`
   - Configure .env file
   - `pip manage.py migrate`
   - `pip manage.py collectstatic`
   - `pip manage.py runserver`
