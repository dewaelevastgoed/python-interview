from django.urls import path

from . import api, views

urlpatterns = [
    path('', views.candidates_list),
    path('api/candidates', api.CandidateListAPI.as_view()),
    path('candidates/<int:pk>/ics/', views.CandidateIcsView.as_view()),
]
