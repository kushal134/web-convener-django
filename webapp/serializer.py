from rest_framework import serializers
from .models import Team


class teamsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Team
        fields = "__all__"


