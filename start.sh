#gunicorn --bind :8000 --timeout 300 app
gunicorn --bind 172.16.78.99:6000 --bind 127.0.0.1:6000 --timeout 300 --workers 5 app

#gunicorn --timeout 300 --bind 172.16.78.98:8000 app
