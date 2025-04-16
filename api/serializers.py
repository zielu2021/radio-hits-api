from rest_framework import serializers
from .models import Artist, Hit


class ArtistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Artist model.
    """
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'created_at', 'full_name']
        read_only_fields = ['created_at', 'full_name']


class HitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Hit model.
    """
    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist',
        write_only=True
    )
    title_url = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Hit
        fields = ['id', 'title', 'artist', 'artist_id', 'title_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'title_url']