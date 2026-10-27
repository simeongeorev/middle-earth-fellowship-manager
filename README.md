# Middle-earth Fellowship Manager

A small Django web app for managing the bands of heroes that protect Middle-earth.
You can create **fellowships**, recruit **characters** into them, and issue **quests**
assigned to one or more fellowships.

## Features

- Full CRUD for fellowships and characters (list, detail, create, edit, delete with confirmation)
- Quests with list, create, edit and delete
- Filter and sort: characters by race / combat power / fellowship, fellowships by origin realm, quests by region / threat level
- A fellowship is marked **Active** automatically while it is assigned to at least one quest
- Cross-field validation: a quest into Mordor cannot have a Low threat level
- Custom `power_stars` template filter that renders a character's combat power as stars
- Custom 404 page, Bootstrap 5 layout with a LOTR theme

## Apps and how they relate

| App | Responsibility |
|---|---|
| `fellowships` | The `Fellowship` model - the base that the other two apps point to |
| `characters` | The `Character` model, linked to a fellowship with a ForeignKey (many characters -> one fellowship) |
| `quests` | The `Quest` model, linked to fellowships with a ManyToManyField (a quest can be assigned to many fellowships and vice versa) |
| `common` | No models. Holds the home page, which shows live counts from all three apps |

```
Character  --(FK)-->  Fellowship  <--(M2M)--  Quest
```

Because of that, the natural order of work in the UI is: create a fellowship first,
then characters and quests that reference it.

## Project structure

```
middle-earth-fellowship-manager/
├── middle_earth_fellowship_manager/   # project settings and root urls
├── characters/                        # app: characters (models, views, forms, templatetags)
├── fellowships/                       # app: fellowships
├── quests/                            # app: quests
├── common/                            # app: home page
├── templates/                         # all templates, incl. base.html and 404.html
├── static/                            # css and js
├── requirements.txt
└── manage.py
```

## Requirements

- Python 3.12 or newer (required by Django 6.1)
- Django 6.1.2 (see `requirements.txt`)
- No environment variables or credentials are needed - the app runs on a local
  SQLite database that Django creates automatically.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/simeongeorev/middle-earth-fellowship-manager.git
   cd middle-earth-fellowship-manager
   ```

2. Check which Python versions you have installed - you need one that is 3.12 or
   newer:

   ```bash
   py --list -p 64         # Windows
   python3 --version       # macOS / Linux
   ```

3. Create and activate a virtual environment using one of the versions listed
   above (the example below uses 3.14 - any 3.12+ works, just swap the number):

   ```bash
   py -3.14 -m venv .venv      # Windows
   python3.14 -m venv .venv    # macOS / Linux
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS / Linux
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply the migrations (this creates the SQLite database):

   ```bash
   python manage.py migrate
   ```

6. Run the app:

   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000/` in your browser. The site starts with an empty
   database - create everything through the navigation links (Fellowships,
   Characters, Quests).

## Notes

- The custom 404 page (`templates/404.html`) is served when `DEBUG = False`.
  With the default `DEBUG = True` setting, Django shows its own debug 404 page.
- The database file `db.sqlite3` is git-ignored and is created on the first migration.
- If `pip install` says Django requires a different Python version, your virtual
  environment was created with Python older than 3.12 - delete the `.venv` folder
  and repeat steps 2-3 with a newer version.
