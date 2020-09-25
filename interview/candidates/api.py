import base64
from tempfile import TemporaryFile

from django.db.models import Q
from django.http import HttpResponse
from rest_framework import serializers, generics
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from ics import Calendar, Event
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateFilter(FilterSet):
    first_name = CharFilter(lookup_expr="icontains")
    last_name = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Candidate
        fields = ("first_name", "last_name")


class CandidateListAPI(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CandidateFilter

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return Candidate.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Candidate.objects.all()


def get_candidate_ics(request, pk):
    c = Calendar()
    candidate = Candidate.objects.get(pk=pk)
    interviews = candidate.interviews.all()
    for interview in interviews:
        e = Event()
        e.name = f"Interview {candidate.full_name}"
        e.begin = interview.time
        c.events.add(e)

    temp_file = TemporaryFile(mode="wb+")
    temp_file.write(bytes(str(c), "utf-8"))
    temp_file.seek(0)
    resp = HttpResponse(temp_file, content_type="text/calendar")
    resp["Content-Disposition"] = "attachment; filename={}".format(f'{candidate.full_name}.ics')
    return resp
