#!/bin/sh

# Load all fixtures in one command
python manage.py loaddata fixtures/category_fixture.json
python manage.py loaddata fixtures/user_fixture.json
python manage.py loaddata fixtures/expense_fixture.json
