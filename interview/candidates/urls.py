from django.urls import path

from . import api, views

urlpatterns = [
    path('', views.candidates_list),
    path('api/candidates', api.CandidateListAPI.as_view()),
    path('api/candidates/<int:pk>/ics', api.get_candidate_ics),
]
