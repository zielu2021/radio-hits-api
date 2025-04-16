from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Artist, Hit


class ModelTestCase(TestCase):
    """Test suite for the Artist and Hit models."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.artist = Artist.objects.create(first_name="Test", last_name="Artist")
        self.hit_title = "Test Song"
        self.hit = Hit.objects.create(title=self.hit_title, artist=self.artist)
    
    def test_model_can_create_artist(self):
        """Test the artist model can create an artist."""
        self.assertEqual(self.artist.full_name, "Test Artist")
    
    def test_model_can_create_hit(self):
        """Test the hit model can create a hit."""
        self.assertEqual(self.hit.title, self.hit_title)
        self.assertEqual(self.hit.artist, self.artist)
        self.assertTrue(self.hit.title_url)


class ViewTestCase(TestCase):
    """Test suite for the API views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.artist = Artist.objects.create(first_name="Test", last_name="Artist")
        self.hit_data = {'title': 'Test Hit', 'artist_id': self.artist.id}
        self.hit = Hit.objects.create(title='Existing Hit', artist=self.artist)
    
    def test_api_can_get_hit_list(self):
        """Test the API can get a list of hits."""
        response = self.client.get(reverse('hit-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_can_create_hit(self):
        """Test the API can create a hit."""
        response = self.client.post(
            reverse('hit-list-create'),
            self.hit_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('title_url' in response.data)
    
    def test_api_can_get_hit_detail(self):
        """Test the API can get a single hit."""
        response = self.client.get(
            reverse('hit-detail', kwargs={'title_url': self.hit.title_url})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.hit.title)
    
    def test_api_can_update_hit(self):
        """Test the API can update a hit."""
        update_data = {'title': 'Updated Hit', 'artist_id': self.artist.id}
        response = self.client.put(
            reverse('hit-detail', kwargs={'title_url': self.hit.title_url}),
            update_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_hit = Hit.objects.get(id=self.hit.id)
        self.assertEqual(updated_hit.title, 'Updated Hit')
        
        print(f"Updated title_url: {updated_hit.title_url}")
        
        self.assertTrue(updated_hit.title_url.startswith('updated-hit'))
    
    def test_api_can_delete_hit(self):
        """Test the API can delete a hit."""
        response = self.client.delete(
            reverse('hit-detail', kwargs={'title_url': self.hit.title_url})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        hit_exists = Hit.objects.filter(id=self.hit.id).exists()
        self.assertFalse(hit_exists)