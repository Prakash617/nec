# nec
sudo fuser -k 8000/tcp

This command will create a file containing all data from your Django project's apps. If you want to backup data for a specific app, you can specify the app name:

python manage.py dumpdata app_name > backup.json
python manage.py loaddata backup.json



django_dbbackup
python manage.py dbbackup --clean --database=your_app_name
python manage.py dbrestore --database=your_app_name


