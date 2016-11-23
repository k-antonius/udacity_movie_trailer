'''
Created on Nov 22, 2016

@author: kennethalamantia
'''


class MovieBuilder(object):
    '''Loads information about a list of movies from a .csv file.
    '''
    
    def __init__(self, csv_file_location):
        '''Initializes a dictionary to hold information from
        a parsed .csv file.
        '''
        self._movie_info = dict()
        self.__csv_file = csv_file_location
        
    def load_info(self):
        '''Parses a csv file for movie information.
        
        Parsed information is stored in self._movie_info.
        '''
        pass
    
    def movie_factory(self):
        '''Creates MovieInfo objects.
        
        Creates a MovieInfo object for each movie stored in the _movie_info 
        field.
        @return - list of MovieInfo objects.
        '''
        pass
    