from django.test import TestCase

from movies.views import CommentRepository
from .models import Movie, Comment

MOVIE_API_RESPONSE_GOOD = {"Title":"Avatar","Year":"2009","Rated":"PG-13","Released":"18 Dec 2009","Runtime":"162 min","Genre":"Action, Adventure, Fantasy","Director":"James Cameron","Writer":"James Cameron","Actors":"Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang","Plot":"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.","Language":"English, Spanish","Country":"UK, USA","Awards":"Won 3 Oscars. Another 85 wins & 128 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.8/10"},{"Source":"Rotten Tomatoes","Value":"83%"},{"Source":"Metacritic","Value":"83/100"}],"Metascore":"83","imdbRating":"7.8","imdbVotes":"992,716","imdbID":"tt0499549","Type":"movie","DVD":"22 Apr 2010","BoxOffice":"$749,700,000","Production":"20th Century Fox","Website":"http://www.avatarmovie.com/","Response":"True"}
MOVIE_API_RESPONSE_BAD = {"Response":"False","Error":"Movie not found!"}

class CommentRepositoryTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="lion")

    def test_saving_comment(self, content = "qwerty", movie_id="1"):
        comment = CommentRepository.save_comment(content, movie_id)
        db_comment = Comment.objects.get(movie_id=movie_id)
        self.assertEqual(comment, db_comment)