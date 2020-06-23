from django.db import models


# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=15)
    team_id = models.CharField(max_length=8)
    team_member_1 = models.CharField(max_length=20)
    team_member_2 = models.CharField(max_length=20)
    team_member_3 = models.CharField(max_length=20)
    team_member_4 = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name
