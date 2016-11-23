'''
Created on Nov 22, 2016

@author: kennethalamantias
'''
import unittest
from movie_trailer_site import movie_builder
import os

# The contents of the test csv file.
# title,description,trailer_url,poster_url
# movie_a,test_description_a,test_trailer_a,test_poster_a
# movie_b,test_description_b,test_trailer_b,test_poster_b
# movie_c,test_description_c,test_trailer_c,test_poster_c

print os.getcwd()
os.chdir("../../data/")
data_dir = os.path.abspath(os.getcwd())
TEST_CSV_LOC = data_dir + "/test_data.csv"

class Test(unittest.TestCase):
    '''Tests the methods from MoiveInfoLoader.
    '''
    def setUp(self):
        self.builder = movie_builder.MovieBuilder(TEST_CSV_LOC)
        self.builder.load_info()
        self.movie_list = self.builder.get_movie_info()
    
    def test_loader(self):
        '''Tests movie_factory method.'''
        
        # Should be three movie objects in list
        self.assertEqual(len(self.builder.get_movie_info()),3)
        self.assertEqual(self.movie_list[0].get_title(), "movie_a")
        self.assertEqual(self.movie_list[1].get_title(), "movie_b")
        self.assertEqual(self.movie_list[2].get_title(), "movie_c")
        self.assertEqual(self.movie_list[0].get_description(), 
                         "test_description_a")
        self.assertEqual(self.movie_list[1].get_trailer(), "test_trailer_b")
        self.assertEqual(self.movie_list[2].get_poster(), "test_poster_c")
        
    def tearDown(self):
        self.builder = None
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    