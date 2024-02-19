from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note, NoteChange

class NoteViewsTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Create a test note
        self.note = Note.objects.create(content='Test Content', owner=self.user)

    def test_create_note(self):
        url = reverse('note-create')
        data = {'content': 'New Note Content'}
        initial_note_count = Note.objects.count()

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), initial_note_count + 1)
        self.assertEqual(Note.objects.last().content, 'New Note Content')


    def test_retrieve_note(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'Test Content')

    def test_update_note(self):
        url = reverse('note-detail', args=[self.note.id])
        data = {'content': 'Updated Note Content'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(id=self.note.id).content, 'Updated Note Content')

    def test_share_note(self):
        # Create another user to share the note with
        shared_user = User.objects.create_user(username='shareduser', password='sharedpass')

        url = reverse('note-share', args=[self.note.id])
        data = {'shared_users': [shared_user.id]}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(shared_user in Note.objects.get(id=self.note.id).shared_users.all())

    def test_version_history(self):
        # Create a note change for the test note
        NoteChange.objects.create(note=self.note, user=self.user, content='Updated Content')

        url = reverse('note-version-history', args=[self.note.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'Updated Content')
