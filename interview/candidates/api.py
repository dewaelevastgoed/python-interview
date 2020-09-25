
from django_filters import rest_framework as filters

from rest_framework import serializers, generics

from django.db.models import Q

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateListAPI(generics.ListAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name')
    serializer_class = CandidateSerializer

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Candidate.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        return Candidate.objects.all()
