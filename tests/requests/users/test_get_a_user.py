import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from klime.models import User, Wall

@pytest.fixture
def Users():
    user1 =  User.objects.create(
        username='Joey',
        email='Joey@joey_mail.com',
    )
    user2 = User.objects.create(
        username='Joanne',
        email='clime@email.com',
    )
    return user1, user2

@pytest.fixture
def Walls(Users):
    user1, user2 = Users
    wall1 = Wall.objects.create(
        name="big WALL",
        photo_url="img.url",
        user=user1,
    )
    wall2 = Wall.objects.create(
        name="big WALL",
        photo_url="img.url",
        user=user2,
    )
    return wall1, wall2

@pytest.mark.django_db
def test_get_a_user_happy(Users, Walls):
    print('test_get_a_user')
    client = APIClient()
    url = reverse('user_details', kwargs={'user_id': 1})
    response = client.get(url)

    assert response.status_code == 200
    assert type(response.json()) is dict
    assert 'data' in response.json()

    assert type(response.json()['data']) is dict
    assert 'id' in response.json()['data']
    assert 'username' in response.json()['data']
    assert 'email' in response.json()['data']
    users_count = User.objects.count()
    assert users_count == 2