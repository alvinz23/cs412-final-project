# 2026 NBA Draft Scouting Database (Django)

A full-stack Django final project for scouting 2026 NBA Draft prospects with CRUD, filtering, and leaderboard reporting.

## Project Structure

```text
.
├── manage.py
├── db.sqlite3 (generated after migrations)
├── README.md
├── draftscout/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── scouting/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   └── management/
│       ├── __init__.py
│       └── commands/
│           ├── __init__.py
│           └── seed_data.py
├── templates/
│   ├── base.html
│   └── scouting/
│       ├── home.html
│       ├── leaderboards.html
│       ├── player_confirm_delete.html
│       ├── player_detail.html
│       ├── player_form.html
│       ├── player_list.html
│       ├── prospect_filter.html
│       ├── report_confirm_delete.html
│       ├── report_detail.html
│       ├── report_form.html
│       ├── team_confirm_delete.html
│       ├── team_detail.html
│       ├── team_form.html
│       └── team_list.html
└── static/
    └── css/
        └── styles.css
```

## Setup and Run Instructions

1. Create and activate a virtual environment.
2. Install Django:
   - `pip install django`
3. Run migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
4. Seed sample data:
   - `python manage.py seed_data`
5. (Optional) Create admin user:
   - `python manage.py createsuperuser`
6. Start development server:
   - `python manage.py runserver`
7. Open app in browser:
   - `http://127.0.0.1:8000/`

## Main Routes

- `/` Home dashboard
- `/prospects/` Prospect list
- `/prospects/filter/` Prospect filtering + sorting
- `/teams/` Team list
- `/leaderboards/` Top overall / shooters / defenders / athletes
- `/admin/` Django admin

