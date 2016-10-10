from django.contrib import admin
from app.models import Team, Player

# Register your models here.
admin.site.register([Team, Player])
