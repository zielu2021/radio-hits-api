from django.urls import path
from .views import HitListCreateView, HitDetailView, ArtistListView, ArtistDetailView

urlpatterns = [
    path('hits/', HitListCreateView.as_view(), name='hit-list-create'),
    path('hits/<str:title_url>/', HitDetailView.as_view(), name='hit-detail'),
    path('artists/', ArtistListView.as_view(), name='artist-list-create'),
    path('artists/<int:id>/', ArtistDetailView.as_view(), name='artist-detail'),
]