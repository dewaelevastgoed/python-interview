from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Candidate


class CandidateTests(TestCase):
    def test_candidate_str(self):
        candidate = Candidate.objects.create(
            first_name="Jack",
            last_name="Sparrow"
        )

        self.assertEqual(
            candidate.__str__(),
            "Jack Sparrow"
        )


class CandidateAPITest(APITestCase):
    def setUp(self):
        Candidate.objects.create(last_name='Sparrow', first_name='Jack')
        Candidate.objects.create(last_name='Kidd', first_name='William')
        
    def test_candidate_list(self):
        """
        Test the candidate listing
        """
        response = self.client.get('/api/candidates')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        candidates = response.json()
        self.assertEqual(len(candidates), 2)
