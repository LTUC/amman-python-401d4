from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model # when called, it returns auth.user model

from django.urls import reverse

from .models import Movie

# Create your tests here.
class MovieTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Samara',
            email = 'samara@gmail.com',
            password = 'Samara123456'
        )
        self.movie = Movie.objects.create(
            name = 'Testing Movie',
            desc = 'For testing purposes',
            director = 'Amarah',
            watcher = self.user
        )

    def test_movie_representation(self):
        expected = 'Testing Movie'
        actual = str(self.movie)
        self.assertEqual(expected, actual)
    
    def test_default_rank(self):
        self.assertEqual(self.movie.rank, 5)
    
    def test_movies_list_view(self):
        response = self.client.get(reverse('movies'))
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Testing Movie')
        self.assertNotEqual(response, 'Django Movie')


    def test_movie_details_view(self):
        response = self.client.get(reverse('movie_details', args="1"))
        no_response = self.client.get('/500')
        self.assertContains(response, 'Amarah')
        self.assertTemplateUsed(response, 'movie_details.html')
        self.assertEqual(no_response.status_code, 404)

    def test_movie_create_view(self):
        response = self.client.post(
            reverse('movie_create'),
            {
                'name': 'testing movie 3',
                'desc' : 'This is to test create view for movie 3',
                'director' : 'Hamza',
                'watcher' : self.user
            }, follow=True
        )

        self.assertContains(response, 'Hamza')
        self.assertRedirects(response, reverse('movie_details', args='2'), status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_movie_update_view(self):
        pass

    def test_movie_delete_view(self):
        pass


    # def test_movies_status_code(self):
    #     expected = 200
    #     actual = self.client.get(reverse('movies')).status_code
    #     self.assertEqual(expected, actual)
    
    # def test_movies_list_queries(self):
    #     response = self.client.get('movies').items()
    #     actual = len(response)
    #     print(actual)
    #     self.assertNumQueries(actual)
    
    # def test_movie_create(self):
    #     response = self.client.post(
    #         reverse('movie_create'), 
    #         {'name':'Testing Movie','desc':'For testing purposes','director':'Amarah', 'watcher':self.user}
    #     )

    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'For testing pu')

    #     get_response = self.client.get(reverse('movies')) 
    #     self.assertEqual(200, get_response.status_code)