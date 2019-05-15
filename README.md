# dj-adminator

Adminator layout compiled to CSS and use with Django based on Adminator-admin-dashboard by puikinsh.

## How to contribute?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/dj-adminator.git
cd dj-adminator
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# python contrib/env_gen.py
python manage.py migrate
```

## I used

https://github.com/puikinsh/Adminator-admin-dashboard/issues/58#issuecomment-366796696

to convert SCSS to CSS.

## TODO

* Fix js
* Fix fonts
