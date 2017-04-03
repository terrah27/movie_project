#define class Movie that will hold all attributes of favorite movies
class Movie():
	def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
		""" This class provides a way to store movie related information """
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
