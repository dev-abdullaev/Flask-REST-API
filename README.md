# Flask-REST-API with MongoDB, Github Actions and AWS CodePipeline

1) Clone the repo - https://github.com/dev-abdullaev/Flask-REST-API.git

2) Run - make build - and you are good to go

3) I set up Github Actions Pipeline to check source code with Pylint

http://127.0.0.1:8080/ - Welcome page

http://127.0.0.1:8080/api/v1/ - Retrive all objects

http://127.0.0.1:8080/api/v1/add/ - Add an object which take key and value 
{
    "key": "Donkey",
    "value": "Domestic"
}

http://127.0.0.1:8080/api/v1/get/{key} - Retrive a single object 
Put  any key whic exists in the db - Donkey for example.

http://127.0.0.1:8080/api/v1/update/{key} - Update object's value and updated_at will also be updated accordingly 
Put  any key whic exists in the db - Donkey for example.
