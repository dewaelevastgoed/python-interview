from django.contrib import admin

from .models import (
    Candidate,
    Interview,
)


class CandidateAdmin(admin.ModelAdmin):
    pass


class InterviewAdmin(admin.ModelAdmin):
    raw_id_fields = ('candidate', )


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Interview, InterviewAdmin)
