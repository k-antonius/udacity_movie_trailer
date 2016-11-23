'''
Module contains a class, MovieInfo, that provides an interface to access the
title, description, trailer, and image poster of one of the movies that is
displayed on the movie trailer site.

Created on Nov 21, 2016
@author: kennethalamantia
'''

class MovieInfo(object):
    '''
    Provides an interface to access information about a movie.
    Instance variables: title, description, trailer, poster
    with getters.
    '''
    
    def __init__(self, title, description, trailer, poster):
        '''
        @param title - movie title
        @param descritpion - movie description
        @param trailer - movie trailer URL
        @param poster - movie image URL
        '''
        
        self._title = title
        self._description = description
        self._trailer = trailer
        self._poster = poster
        
    def __repr__(self):
        '''String representation of MovieInfo object.'''
        
        return "MovieInfo( " + self._title + " " + self._description + ")"
    
    def get_title(self):
        '''Returns the title of the movie.'''
        
        return self._title
    
    def get_description(self):
        '''Returns the text description of the movie.'''
        
        return self._description
    
    def get_trailer(self):
        '''Returns the URL of the move's trailer video.'''
        
        return self._trailer
    
    def get_poster(self):
        '''Returns the URL of the movie's image poster.'''
        
        return self._poster
    