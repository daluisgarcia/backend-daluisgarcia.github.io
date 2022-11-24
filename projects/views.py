from django.views.generic import ListView

from .models import Project


class ListProjectsView(ListView):
    model = Project
    template_name = 'projects/index.html'