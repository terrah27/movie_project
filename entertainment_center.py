import media
import fresh_tomatoes

#create instance of class Movie for each movie
jackie = media.Movie("Jackie",
                     "http://www.impawards.com/2016/posters/jackie.jpg",
                     "https://youtu.be/7cdzT05HpS4")

moonlight = media.Movie("Moonlight",
	                    "http://www.impawards.com/2016/posters/moonlight_ver2.jpg",
	                    "https://youtu.be/9NJj12tJzqc")

little_mermaid = media.Movie("The Little Mermaid",
	                         "https://images-na.ssl-images-amazon.com/images/M/MV5BODMyNjI5ZjMtNTJmYi00MmEwLWIwYmUtZTgyMzg2OWExNzEzXkEyXkFqcGdeQXVyNjQ3NTcyNzQ@._V1_SY132_CR0,0,89,132_AL_.jpg",
	                         "https://youtu.be/wWhmheEtIdI")

#create list of movies
movies = [jackie, moonlight, little_mermaid]

#give list of movies to fresh_tomatos module
fresh_tomatoes.open_movies_page(movies)