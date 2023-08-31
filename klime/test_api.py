import requests
from django.contrib.auth.models import User
from django.test import Client
import code 
# from klime.models import User  

# ENDPOINT = "https://klime-be.onrender.com/users/1/walls/1/"
ENDPOINT = "http://127.0.0.1:8000/users/"
def test_can_get_walls():
    user = User.objects.get(username='username')
    code.interact(local=dict(globals(), **locals()))
    response = requests.get(ENDPOINT)
    assert response.status_code == 200 
    
# def test_can_create_problem():
#     payload = {
#     "data": [
#         {
#             "name": "Joey does vectors ",
#             "vectors": "veecctorssss",
#             "wall_id": 1
#         }
#             ]
#               }
#     create_problem_response = requests.put(ENDPOINT + "problems", json=payload)
#     assert create_problem_response.status_code == 200 

#     data = create_problem_response.json()
#     problem_id = data["data"]["id"]

#     get_problem_response = requests.get(ENDPOINT + f"problems/{problem_id}")
#     assert get_problem_response.status_code == 200
#     get_problem_data = get_problem_response.json()

#     assert get_problem_data["data"]["name"] == payload["data"]["name"]


