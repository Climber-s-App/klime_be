from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username
class Wall(models.Model):
    name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Problem(models.Model):
    name = models.CharField(max_length=50)
    vectors = models.JSONField()
    grade = models.CharField(max_length=10, null=True)
    wall_id = models.ForeignKey(Wall, on_delete=models.CASCADE)

    def __str__(self):
        return self.name