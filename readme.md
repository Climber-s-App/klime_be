# Klime 

## About This Project
Important to Note 
This app needs both this repo (back end) AND https://github.com/Climber-s-App/klime_fe (front end) in order to be fully functioning. 

## Mod 4 Capstone Project 
Klime is an app that enables a user to take a picture of their bouldering wall and create custom climbing routes. 

<br> The backend handles the database for Users, Walls, and Problems

## This Project Utilizes 

* ![Python](https://img.shields.io/badge/Python-blue)
* ![Django](https://img.shields.io/badge/Django-red)
* ![PostGresql](https://img.shields.io/badge/PostGresql-purple)
* ![Render](https://img.shields.io/badge/Render-blue)
* ![VisualCodeStudio](https://img.shields.io/badge/VSCode-pink)
* ![Postman Badge](https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=fff&style=for-the-badge)

## Running On
- Python 3.11.4
- Django 4.2.4

## Getting Started 
### Installation 
1. Fork the Project
2. Clone Repo 

```git clone git@github.com:Climber-s-App/klime_be.git```

3. Install requirements 

```pip install -r requirements.txt```

4. Create and Activate Virtual Environment 

```python3 -m venv .venv```

```. .venv/bin/activate```

5. Make Database 

```python manage.py makemigrations```
```python manage.py migrate```

## Endpoints Used 
<div style="overflow: auto; height: 200px;">
  <pre>
    <code>
    get '/api/v0/users/' -- Gets all users
    get '/api/v0/users/:user_id/' -- Gets specific user by ID
    get '/api/v0/users/:user_id/walls/' -- Gets specific users walls 
    get '/api/v0/users/:user_id/walls/:wall_id/' -- Gets specific wall owned by user 
    get '/api/v0/users/:user_id/walls/:wall_id/problems/' -- Gets all problem belonging to a users wall
    post '/api/v0/users/:user_id/walls/:wall_id/problems/' -- Posts a problem to a users wall
    get '/api/v0/users/:user_id/walls/:wall_id>/problems/:problem_id/' -- Gets a specific problem from a users wall
    </code>
  </pre>
</div>

## Schema 

```Users: name, email```

```Walls: name, photo_url, user_id```

```Problems: name, vectors, wall_id```

## Authors 
- Blaine Glasgow [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GlowMunch)[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/blaine-glasgow-134a9017a/)

- Jesse Thomas [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.linkedin.com/in/jesse-g-thomas/)[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://github.com/jgthomas-12)

- Nick Tassinari [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NickTassinari)[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tassinarinicholas/)
