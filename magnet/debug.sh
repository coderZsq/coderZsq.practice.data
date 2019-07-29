gunicorn -w 4 -b 172.19.189.121:5003 --access-logfile ./logs/log magnet:app
