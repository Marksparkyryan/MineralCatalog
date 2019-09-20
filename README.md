# MineralCatalog

Mineral Catalogue is a simple Django app that displays over 800 minerals and their attributes. Mineral data is loaded into the database from a Json file. Attributes are shown if they're available. Available attributes are sorted by length of data. There's also a random feature that retrieves a random mineral in the database and displays its attributes. There are a few examples of custom template filters as well. 


<br/>

# installation

1. cd into your directory of projects (or wherever you prefer to keep your clones)
2. git clone ```https://github.com/Marksparkyryan/MineralCatalog.git``` to clone the app
3. ```virtualenv .venv``` to create your virtual environment
4. ```source .venv/bin/activate``` to activate the virtual environment
5. ```pip install -r MineralCatalog/requirements.txt``` to install app requirements
6. cd into the MineralCatalog/mineral_site directory
7. ```python manage.py migrate``` to apply the existing data and model migrations
8. ```python manage.py runserver``` to serve the site to your local host (in DEBUG mode)
9. visit ```http://127.0.0.1:8000/``` to see some minerals! 


<br/>

# usage

By default, DEBUG mode is set to True in settings.py. This is good for testing but not good for deployment. If deploying, make sure
DEBUG is set to False.

If deploying, the secret key should be replaced in settings.py - ideally inside an environment variable.


<br/>

# screenshots

<img width="412" alt="Screen Shot 2019-09-20 at 4 26 13 PM" src="https://user-images.githubusercontent.com/45185244/65356836-67515580-dbc3-11e9-827e-e258cd59d0c1.png">

<br/>

<img width="412" alt="Screen Shot 2019-09-20 at 4 27 40 PM" src="https://user-images.githubusercontent.com/45185244/65356912-98ca2100-dbc3-11e9-9cc5-cf1703ee025f.png">

<br/>

<img width="413" alt="Screen Shot 2019-09-20 at 4 30 11 PM" src="https://user-images.githubusercontent.com/45185244/65357060-f3637d00-dbc3-11e9-99de-7b9a7777560a.png">

<br/>


# credits

https://www.w3schools.com/howto/howto_js_scroll_to_top.asp for the appear/dissappear feature on the back-to-top arrow on the mineral list page

Treehouse Techdegree Project 6
