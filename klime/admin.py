from django.contrib import admin
from .models import User, Wall, Problem

admin.site.register(User)
admin.site.register(Wall)
admin.site.register(Problem)