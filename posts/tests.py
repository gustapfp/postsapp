
from django.test import TestCase
from .models import Posts

class PostModelTest(TestCase):
    def setUp(self) -> None:
        Posts.objects.create(text='just a test') # ModelName.Objects
    
    def test_text_content(self): 
        posts = Posts.objects.get(id=1)
        expected_object_name = f'{posts.text}'
        self.assertEqual(expected_object_name, "just a test")