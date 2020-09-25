
from ics import Calendar, Event

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from candidates.models import Candidate


def candidates_list(request):
    return render(request, "candidates/list.html", {})


class CandidateIcsView(DetailView):
    model = Candidate
    template_name = 'candidates/candidate_ics.html'

    def get(self, request, *args, **kwargs):
        candidate = self.get_object()
        calendar = Calendar()
        for interview in candidate.interviews.all():
            event = Event()
            event.name = f"Interview with {candidate.first_name} {candidate.last_name}"
            event.begin = interview.time
            calendar.events.add(event)

        response = HttpResponse()
        response.write(calendar)
        response['Filename'] = 'interviews.ics'  # IE needs this
        response['Content-Disposition'] = 'attachment; filename=filename.ics'
        return response
