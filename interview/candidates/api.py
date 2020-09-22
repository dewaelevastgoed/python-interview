from rest_framework import serializers, generics

from .models import Candidate

   
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateListAPI(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
