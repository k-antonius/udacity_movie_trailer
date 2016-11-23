'''
Created on Nov 22, 2016

@author: kennethalamantias
'''
import unittest
from movie_trailer_site import movie_builder, movie_info

# The contents of the test csv file.
'''
title,description,trailer_url,poster_url
movie_a,test_description_a,test_trailer_a,test_poster_a
movie_b,test_description_b,test_trailer_b,test_poster_b
movie_c,test_description_c,test_trailer_c,test_poster_c
'''
TEST_CSV_LOC = "../data/test_data.csv"

class Test(unittest.TestCase):
    '''Tests the methods from MoiveInfoLoader.
    '''
    def setUp(self):
        self.builder = movie_builder.MovieBuilder(TEST_CSV_LOC)
        self.builder.load_info()
        self.movie_list = self.builder.movie_factory()

    def test_loader_dict(self):
        '''Tests correctness of info loaded by MovieInfoLoader.
        
        Tests various expected key/value pairs in the dictionary.
        '''
        
        self.assertEqual(self.builder._movie_info["movie_a"],{"description" :
                                                         "test_description_a",
                                                         "trailer_url" : 
                                                         "test_trailer_a",
                                                         "poster_url" :
                                                         "test_poster_a"}
                         )
        self.assertEqual(self.builder._movie_info["movie_b"],{"description" :
                                                         "test_description_b",
                                                         "trailer_url" : 
                                                         "test_trailer_b",
                                                         "poster_url" :
                                                         "test_poster_b"}
                         )
        self.assertEqual(self.builder._movie_info["movie_c"],{"description" :
                                                         "test_description_c",
                                                         "trailer_url" : 
                                                         "test_trailer_c",
                                                         "poster_url" :
                                                         "test_poster_c"}
                         )
    
    def test_factory(self):
        '''Tests movie_factory method.'''
        
        # Should be three movie objects in list
        self.assertEqual(len(self.builder.movie_factory()),3)
        self.assertEqual(self.movie_list[0],movie_info.MovieInfo("movie_a",
                                                      "test_description_a",
                                                      "test_trailer_a",
                                                      "test_poster_a"))
        self.assertEqual(self.movie_list[1],movie_info.MovieInfo("movie_b",
                                                      "test_description_b",
                                                      "test_trailer_b",
                                                      "test_poster_b"))
        self.assertEqual(self.movie_list[2],movie_info.MovieInfo("movie_c",
                                                      "test_description_c",
                                                      "test_trailer_c",
                                                      "test_poster_c"))
        
    def tearDown(self):
        self.builder = None
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    