from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    """
    View for the homepage.
    """
    template_name = 'index.html'


class HitsListView(TemplateView):
    """
    View for the hits list page.
    """
    template_name = 'hits/list.html'


class HitDetailView(TemplateView):
    """
    View for the hit detail page.
    """
    template_name = 'hits/detail.html'


class ArtistsListView(TemplateView):
    """
    View for the artists list page.
    """
    template_name = 'artists/list.html'