from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Hit, Artist
from .serializers import HitSerializer, ArtistSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404


class HitListCreateView(ListCreateAPIView):
    """
    API view to retrieve list of hits or create a new hit.
    """
    queryset = Hit.objects.all()
    serializer_class = HitSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HitDetailView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a hit.
    """
    serializer_class = HitSerializer
    lookup_field = 'title_url'

    def get_queryset(self):
        return Hit.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ArtistListView(ListCreateAPIView):
    """
    API view to retrieve list of artists or create a new artist.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete an artist.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'id'