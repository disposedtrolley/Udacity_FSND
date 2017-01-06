import media
import fresh_tomatoes
import requests
import re

BASEURL_OMDB = "http://www.omdbapi.com/"	# baseurl of the OMDb API
BASEURL_YOUTUBE = "http://www.youtube.com/results"	# baseurl of YouTube search

# array of movie names
MOVIE_NAMES = ["Train to Busan",
			   "Your Name",
			   "The Babadook",
			   "Ghost in the Shell",
			   "The Shining",
			   "Rogue One"]

movie_objects = []		# array of Movie objects

# iterate through the MOVIE_NAMES array
for movie_name in MOVIE_NAMES:
	params_omdb = {"t": movie_name,
				   "y": "",
				   "plot": "short",
				   "r": "json"}

	# grab movie details from OMDb API, converted to Python dictionary
	movie_info = requests.get(BASEURL_OMDB, params=params_omdb).json()

	# Get the trailer from YouTube by querying the movie title and returning
	# the URL of the first result.
	# Partial code from
	# https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
	params_youtube = {"search_query": movie_info["Title"] + " trailer"}
	trailer_results = requests.get(BASEURL_YOUTUBE, params=params_youtube).text
	video_urls = re.findall(r'href=\"\/watch\?v=(.{11})', trailer_results)
	trailer_url = "http://www.youtube.com/watch?v=" + video_urls[0]

	# append new Movie object to the array
	movie_objects.append(media.Movie(movie_info["Title"],
							  movie_info["Plot"],
							  movie_info["Poster"],
							  trailer_url))

# render and open the movies website
fresh_tomatoes.open_movies_page(movie_objects)