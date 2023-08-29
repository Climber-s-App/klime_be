import pytest

from django.contrib.auth.models import User


# def check_user_creation(user_1):
#     print ("check_username")
#     assert user_1.username == "User_Joey"

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test_user', 'test@email.com')
    count = User.objects.all().count()
    print(count)
    assert User.objects.count() == 1
