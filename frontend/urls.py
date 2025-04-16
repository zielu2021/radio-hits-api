from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hits/', views.HitsListView.as_view(), name='hits'),
    path('hits/<str:title_url>/', views.HitDetailView.as_view(), name='hit_detail'),
    path('artists/', views.ArtistsListView.as_view(), name='artists'),
]