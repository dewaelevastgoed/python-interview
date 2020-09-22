from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def print_interview(self):
        print("Interviews for candidate " + self.first_name + " " + self.last_name)
        index = 1
        for interview in self.interviews.all():
            print(index + " - " + interview.time)


class Interview(models.Model):
    STATE_SCHEDULED = 1
    STATE_FINISHED = 2

    STATES = (
        (STATE_SCHEDULED, 'Scheduled'),
        (STATE_FINISHED, 'Finished'),
    )

    candidate = models.ForeignKey(Candidate, related_name='interviews', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(default=STATE_SCHEDULED, choices=STATES)
    time = models.DateTimeField()
    feedback = models.TextField(default='', blank=True)
