
from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    PageVisit.objects.create()
    return render(request, 'home.html', {'count': queryset.count()})
