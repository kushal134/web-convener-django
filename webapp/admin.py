from django.contrib import admin
from . models import Team



class TeamsAdmin(admin.ModelAdmin):
    list_display = ("team_name", "team_id")


admin.site.register(Team, TeamsAdmin)


