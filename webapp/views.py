from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Team
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializer import teamsSerializer


def index(request):
    itsp_teams = Team.objects.all()
    return render(request, "index.html", {"teams": itsp_teams})




class TeamList(APIView):

    def get(self,request,my_id):
        itsp_teams = Team.objects.get(team_id=my_id)
        serializer = teamsSerializer(itsp_teams)
        return Response(serializer.data)

    def post(self):
        pass


# For displaying information of all teams
class TeamListAll(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = teamsSerializer

# class TeamListAll(APIView):
#
#     def get(self,request):
#         itsp_teams = Team.objects.all()
#         serializer = teamsSerializer(itsp_teams,many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass

