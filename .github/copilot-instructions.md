## Copilot instructions for the MeuFluxo repository

Purpose: help AI coding agents become productive quickly in this Django project.

- **Big picture**: This is a small Django site (single project) using SQLite and one primary app `accounts`.
  - Top-level URLs: `MeuFluxo/urls.py` includes `accounts.urls` at the root.
  - App-level entrypoint: `accounts/views.py` contains simple function-based views (e.g. `login_view`).
  - Templates: global templates live under `templates/` (see `templates/base.html` and `templates/registration/login.html`), and app templates follow the Django app layout `accounts/templates/accounts/*.html` (views render `accounts/login.html`).
  - Settings: `MeuFluxo/settings.py` uses `sqlite3` (db file at project root), `DEBUG = True`, `LANGUAGE_CODE = 'pt-br'`, and `TIME_ZONE = 'America/Sao_Paulo'`.

- **Developer workflows & commands (Windows / this repo)**:
  - Activate venv (bash): `. venv/Scripts/activate`
  - Activate venv (PowerShell/CMD): `.\\venv\\Scripts\\activate`
  - Run migrations: `py manage.py migrate`
  - Create app (example used here): `py manage.py startapp accounts`
  - Run dev server: `py manage.py runserver`
  - Run tests: `py manage.py test`
  - Create superuser: `py manage.py createsuperuser`

- **Project-specific conventions & patterns**:
  - Minimal app structure: most logic lives in `accounts/` (views, templates). Prefer editing `accounts/views.py`, `accounts/urls.py` and templates for UI changes.
  - Templates are served with `APP_DIRS = True` and no extra `TEMPLATES['DIRS']` configured—put app templates under `accounts/templates/accounts/` or use the project `templates/` folder for shared pages.
  - Static assets are served from the `static/` folder; some UI uses CDN (Tailwind + Lucide) in `templates/base.html`.
  - Internationalization is Portuguese-first: keep messages/labels in Portuguese where present.

- **Integration points & external deps**:
  - No recorded pip manifest in the repo; assume Django is required. The settings file header references Django 6.0.2—verify installed Django version in the virtualenv.
  - UI loads Tailwind and Lucide from CDNs (internet access required for styling/icons).

- **Editing guidance — concrete examples**:
  - To change the login page UI, edit `templates/registration/login.html` or `accounts/templates/accounts/login.html` and `accounts/views.py` if you need to change context.
  - To add a new top-level route, update `MeuFluxo/urls.py` and add `include('<app>.urls')`.
  - To add models, update `accounts/models.py`, run `py manage.py makemigrations` and `py manage.py migrate`.

- **Safety notes**:
  - `MeuFluxo/settings.py` currently contains a development secret key and `DEBUG = True`. Do not publish production secrets or flip `DEBUG` without preparing proper deployment settings.

If any of these areas are unclear or you'd like the instructions to emphasize other workflows (tests, CI, deploy), tell me which parts to expand or correct.
