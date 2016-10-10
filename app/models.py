from django.db import models

# Create your models here.
class Team(models.Model):
    year = models.IntegerField()
    win = models.IntegerField()
    loss = models.IntegerField()
    bowl_game = models.CharField(max_length=30)
    coach = models.CharField(max_length=30)

    def __str__(self):
        return str(self.year)

class Player(models.Model):
    player_year = models.ForeignKey(Team)
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    position = models.CharField(max_length=2)

    def __str__(self):
        return self.name
