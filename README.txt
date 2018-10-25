docker run --name online-exam-db -p 5432:5432 -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres
docker run --name online-exam-db -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres
 
$env:FLASK_APP = "./src/main.py"
pipenv --venv
. C:\Users\BogdanFlorinAlbu\.virtualenvs\backend-WMBvRIUN\Scripts\activate.bat
flask run -h 127.0.0.1

cd backend
pipenv --three
pipenv install sqlalchemy psycopg2-binary
pipenv shell
pipenv install flask marshmallow
pipenv install flask-cors

# activate virtual environment
pipenv shell
# run main module
python -m src.main


#erori

lalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused (0x0000274D/10061)
        Is the server running on host "127.0.0.1" and accepting
        TCP/IP connections on port 5432?
 (Background on this error at: http://sqlalche.me/e/e3q8)
 
 sau
 
 C:\Program Files\Docker\Docker\Resources\bin\docker.exe: Error response from daemon: driver failed programming external connectivity on endpoint agitated_booth (87e23466b5c165712c3ef89e0315e365dc16a36f1ce2f3132443360aab1af631): Error starting userland proxy: mkdir /port/tcp:0.0.0.0:8080:tcp:172.17.0.2:8080: input/output error.
 
 =>
 
 docker restart
 docker run --name online-exam-db -p 5432:5432 -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres
 
curl http://127.0.0.1:5000/exams
