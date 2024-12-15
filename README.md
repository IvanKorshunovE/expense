# ExpenseTracker

Simple app

## Requirements
- Python 3.x
- Django
- Django REST framework

# Steps to Set Up the Project
git clone https://github.com/IvanKorshunovE/expense
cd expense
nano .env
set up .env file from env-example
docker-compose -f ./docker/docker-compose.yml up --build -d
docker-compose -f ./docker/docker-compose.yml expense_app python manage.py loaddata fixtures/category_fixture.json