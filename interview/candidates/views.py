from django.shortcuts import render


def candidates_list(request):
    return render(request, "candidates/list.html", {})
