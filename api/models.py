from django.db import models
from django.utils.text import slugify
import re


class Artist(models.Model):
    """
    Model representing a music artist.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Hit(models.Model):
    """
    Model representing a hit song.
    """
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, related_name='hits', on_delete=models.CASCADE)
    title_url = models.SlugField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def save(self, *args, **kwargs):
        """
        Override save method to automatically generate title_url if not provided
        or when title changes.
        """
        # Check if this is update, if title was changed initiate empty str to regenerate url
        if self.pk:
            original = Hit.objects.get(pk=self.pk)
            if original.title != self.title:
                self.title_url = ''
        
        # Logic to generate title_url
        if not self.title_url:
            slug = slugify(self.title)
            
            # Check if similar url already exists- if exists then add suffix
            similar_slugs = Hit.objects.filter(title_url__startswith=slug).values_list('title_url', flat=True)
            
            if not similar_slugs or slug not in similar_slugs:
                self.title_url = slug
            else:
                pattern = f"^{re.escape(slug)}(-[0-9]+)?$"
                existing_slugs = [s for s in similar_slugs if re.match(pattern, s)]
                
                if not existing_slugs:
                    self.title_url = slug
                else:
                    # In case if this url exists find the max sufix and increment
                    highest = 0
                    for existing in existing_slugs:
                        match = re.match(f"^{re.escape(slug)}-([0-9]+)$", existing)
                        if match:
                            highest = max(highest, int(match.group(1)))
                    
                    self.title_url = f"{slug}-{highest + 1}"
        
        super().save(*args, **kwargs)