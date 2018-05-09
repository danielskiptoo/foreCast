ENGINE= 'django.db.backends.postgresql',
DB_NAME= 'finalP'
DB_USER= 'postgres'
DB_PASSWORD= 'root@k'
DB_HOST= '127.0.0.1'
DB_PORT= '5432'


ALLOWED_HOSTS = ['forecas.herokuapp.com','127.0.0.1']


SECRET_KEY = 'rz&mw1v(5*-g8c0-z5j40y6(imdzxln19c*_mu8v%_j-&2y_q@'

#EMAIL_FILE_PATH = '/tmp/app-messages'

#DEFAULT_FROM_EMAIL = EMAIL_HOST_USERWSGI_APPLICATION = 'app.wsgi.application'

#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_HOST_USER = 'danielkipson011@gmail.com'
#EMAIL_FILE_PATH = '/tmp/app-messages'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'parsifal_app'
EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
EMAIL_USE_TLS = True
