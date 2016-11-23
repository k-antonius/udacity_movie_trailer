'''
Created on Nov 22, 2016

@author: kennethalamantia
'''

import csv
from movie_trailer_site import movie_info

TITLE = 0
DESCRIPTION = 1
TRAILER = 2
POSTER = 3

class MovieBuilder(object):
    '''Loads information about a list of movies from a .csv file.
    '''
    
    def __init__(self, csv_file_location):
        '''Initializes a dictionary to hold information from
        a parsed .csv file.
        '''
        self._movie_info = list()
        self.__csv_file = csv_file_location
        
    def load_info(self):
        '''Parses a csv file for movie information.
        
        Parsed information is stored in self._movie_info.
        '''
        with open(self.__csv_file,"r") as data_file:
            reader = csv.reader(data_file)
            # headers in csv file:
            # title, description, trailer_url, poster_url
            dummy_header = reader.next()
            for row in reader:
                self._movie_info.append(movie_info.MovieInfo(row[TITLE],
                                                             row[DESCRIPTION],
                                                             row[TRAILER],
                                                             row[POSTER])
                                        )
            
    def get_movie_info(self):
        '''Creates MovieInfo objects.
        
        Creates a MovieInfo object for each movie stored in the _movie_info 
        field.
        @return - list of MovieInfo objects.
        '''
        return self._movie_info
