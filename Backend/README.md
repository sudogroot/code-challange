# Book Backend #

## Getting started ##

#### Development ####

 ```sh
pip install -r requirements-dev.txt
 
 ```


than  run : init.sh

#### Production ####

 ```sh
 pip install -r requirements.txt
 
 manage.py makemigrations
 
 manage.py migrate
 
 ```



## Testing ##



 ```sh
pytest 
 ```

test withi coverage :

 ```sh
pytest --cov=books
 ```
 


## TODOs ##

- Optimize production settings including change data base production 
- Make request validation
- Create makefile
- Optimize comments and stars Views group them by book
- Optimize testing coverage
