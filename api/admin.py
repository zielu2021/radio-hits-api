from django.contrib import admin
from .models import Artist, Hit


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')


@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'created_at', 'updated_at')
    list_filter = ('artist',)
    search_fields = ('title', 'artist__first_name', 'artist__last_name')
    prepopulated_fields = {'title_url': ('title',)}
    ordering = ('-created_at',)