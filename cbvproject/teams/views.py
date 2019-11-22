from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

# from .mixins import PageTitleMixin
from . import models


class TeamListView(CreateView, ListView):
    context_object_name = 'teams'
    fields = ('name', 'practice_location', 'coach')
    model = models.Team
    template_name = 'teams/team_list.html'