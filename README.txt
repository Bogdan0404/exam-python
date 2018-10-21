 $env:FLASK_APP = "./src/main.py"
 pipenv --venv
 . C:\Users\BogdanFlorinAlbu\.virtualenvs\backend-WMBvRIUN\Scripts\activate.bat
flask run -h 127.0.0.1

pipenv --three
pipenv install sqlalchemy psycopg2-binary
pipenv shell
pipenv install flask marshmallow
pipenv install flask-cors

curl http://127.0.0.1:5000/exams
