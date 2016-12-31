import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story, avatar]

# fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)