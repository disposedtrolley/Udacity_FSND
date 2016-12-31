# Movie Trailer Website

Hello! This is my attempt at the Movie Trailer Website project, using the [OMDb API](https://www.omdbapi.com/) to retrieve data on films, and the [Requests](http://docs.python-requests.org/en/master/) Python library to make HTTP requests and parse the JSON results.

Since the API doesn't provide URLs to the movie trailers, I've taken a few lines of code from [here](https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video) to perform a YouTube query for the trailer of each movie, and return the URL of the first result.

I've used the Superhero Bootstrap theme from [Bootswatch](https://bootswatch.com/#) and modified the CSS slightly to accomodate the changes. I've included the storyline below each movie's title.

Enjoy!

## Getting Started

1. Ensure the latest version of Python 2.7 is installed on your system.
2. [Install](http://docs.python-requests.org/en/master/user/install/#install) the Requests HTTP library
3. Download and extract the project files
4. Navigate to the project directory and execute `driver.py` to launch the website