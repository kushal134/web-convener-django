from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views



urlpatterns = [
    path("all", views.TeamListAll.as_view()),
    path("<str:my_id>", views.TeamList.as_view()),
    path("", views.index)
]



