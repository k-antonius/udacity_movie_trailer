'''
Created on Nov 21, 2016

@author: kennethalamantia
'''

class Movie(object):
    '''
    Provides an interface to access information about a movie.
    '''


    def __init__(self, title):
        '''
        Constructor
        '''
        self._title = title