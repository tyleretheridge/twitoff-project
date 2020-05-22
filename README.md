# twitoff-project

## Installation
1. Clone repo
2. Install dependencies and packages from pipfile
3. Setup database

To create migration folder:   
```
FLASK_APP=web_app flask db init 
```

To change or update database schema:  
```
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade 
```
Migrate will create the database.  
Upgrade will create the tables.  


## Usage
```sh
# mac version:
FLASK_APP=web_app flask run
# windows version:
set FLASK_APP=web_app
flask run
```   
For local usage (non-production server), navigate to [localhost:5000/](http://localhost:5000/) in a web browser.  

Otherwise navigate to your production server domain. 