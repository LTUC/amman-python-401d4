from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'Walking at night in Down Town',
            body = 'It feel good when you walk at night, espcially with a cup of coffee'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_title, 'Walking at night in Down Town')
        self.assertEqual(actual_body, 'It feel good when you walk at night, espcially with a cup of coffee')