'''
Loads the movie trailer website.
Uses the information located in the movie_data.csv file in
the data directory of the module.

Created on Nov 22, 2016
@author: kennethalamantia
'''

import pkg_resources
from movie_trailer_site import movie_builder, fresh_tomatoes

def load_movie_trailer_site():
    '''Loads the movie trailer website.'''

    rm = pkg_resources.ResourceManager()
    data_file = rm.resource_stream("movie_trailer_site",
                                   "/data/movie_data.csv")
    data_loader = movie_builder.MovieBuilder(data_file)
    data_loader.load_info()
    fresh_tomatoes.open_movies_page(data_loader.get_movie_info())


