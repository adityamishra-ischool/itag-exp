#!flask/bin/python
# this file will be our executable..and import the App package to autoconfig and RuntimeError

from app import app
from app import views

app.run(debug=True)
