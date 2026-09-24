from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User
from categories.models import Category
from .models import Place

class PlaceApiTests(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='VibeKigali2026')
        self.other = User.objects.create_user(username='other', password='VibeKigali2026')
        self.category = Category.objects.create(name='Restaurants', slug='restaurants')
        self.place = Place.objects.create(
            name='Repub Lounge',
            description='Rwandan food with a view.',
            category=self.category,
            address='KN 3 Ave, Kigali',
            owner=self.owner,
        )

    def payload(self, **overrides):
        data = {
            'name': 'Question Coffee',
            'description': 'Specialty coffee downtown.',
            'category_id': self.category.id,
            'address': 'KN 78 St, Kigali',
        }
        data.update(overrides)
        return data

    def test_anyone_can_list_places(self):
        response = self.client.get(reverse('place-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_anonymous_user_cannot_create_place(self):
        response = self.client.post(reverse('place-list'), self.payload())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logged_in_user_creates_place_and_becomes_owner(self):
        self.client.force_authenticate(user=self.other)
        response = self.client.post(reverse('place-list'), self.payload())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.get(name='Question Coffee').owner, self.other)

    def test_owner_can_update_own_place(self):
        self.client.force_authenticate(user=self.owner)
        url = reverse('place-detail', args=[self.place.id])
        response = self.client.patch(url, {'name': 'Repub Lounge Kigali'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.place.refresh_from_db()
        self.assertEqual(self.place.name, 'Repub Lounge Kigali')

    def test_other_user_cannot_update_place(self):
        self.client.force_authenticate(user=self.other)
        url = reverse('place-detail', args=[self.place.id])
        response = self.client.patch(url, {'name': 'Hacked'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_other_user_cannot_delete_place(self):
        self.client.force_authenticate(user=self.other)
        response = self.client.delete(reverse('place-detail', args=[self.place.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_can_delete_own_place(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(reverse('place-detail', args=[self.place.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Place.objects.count(), 0)

    def test_cannot_set_owner_from_request_body(self):
        self.client.force_authenticate(user=self.other)
        response = self.client.post(reverse('place-list'), self.payload(owner=self.owner.id))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.get(name='Question Coffee').owner, self.other)
