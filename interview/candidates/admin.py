from django.contrib import admin

from .models import Candidate, Interview


class InterviewInline(admin.TabularInline):
    model = Interview
    extra = 1

class CandidateAdmin(admin.ModelAdmin):
    inlines = [
        InterviewInline
    ]

admin.site.register(Candidate, CandidateAdmin)
