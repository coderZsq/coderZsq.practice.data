gunicorn -w 4 -b 172.19.189.121:5001 -D --access-logfile ./logs/log magnet:app
gunicorn -w 4 -b 172.19.189.121:5002 -D --access-logfile ./logs/log magnet:app
