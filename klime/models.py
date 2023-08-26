from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username
class Wall(models.Model):
    name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=1000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name