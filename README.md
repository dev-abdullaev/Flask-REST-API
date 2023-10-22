# Flask-REST-API with MongoDB

1) Clone the repo - https://github.com/dev-abdullaev/Flask-REST-API.git

2) Run - make build - and you are good to go

http://127.0.0.1:8080/ - Welcome page

http://127.0.0.1:8080/api/v1/ - Retrive all objects

http://127.0.0.1:8080/api/v1/add/ - Add an object which take key and value - Example below
{
    "key": "Donkey",
    "value": "Domestic"
}

http://127.0.0.1:8080/api/v1/get/{key} - Example below put Donkey instead of key

http://127.0.0.1:8080/api/v1/update/{key} - Example below, put again Donkey instead of key

