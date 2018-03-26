# Drop DB  first
echo "-> make migrations"
python manage.py makemigrations
echo "-> load migrations"
python manage.py migrate
echo "-> load inital books and comments"
python manage.py loaddata initial_books --traceback
