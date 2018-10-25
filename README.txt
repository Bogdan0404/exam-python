docker run --name online-exam-db -p 5432:5432 -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres
docker run --name online-exam-db -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres
 
$env:FLASK_APP = "./src/main.py"
pipenv --venv
. C:\Users\BogdanFlorinAlbu\.virtualenvs\backend-WMBvRIUN\Scripts\activate.bat
flask run -h 127.0.0.1

pipenv --three
pipenv install sqlalchemy psycopg2-binary
pipenv shell
pipenv install flask marshmallow
pipenv install flask-cors

python -m src.main

curl http://127.0.0.1:5000/exams
