
from django.test import TestCase
from .models import Posts
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self) -> None:
        Posts.objects.create(text='just a test')
    
    def test_text_content(self): 
        posts = Posts.objects.get(id=1)
        expected_object_name = f'{posts.text}'
        self.assertEqual(expected_object_name, "just a test")

class PageViewTest(TestCase):
    def setUp(self): 
        Posts.objects.create(text='this is another test.')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/') 
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_user_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')