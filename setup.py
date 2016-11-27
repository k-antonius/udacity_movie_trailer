'''
Created on Nov 26, 2016

@author: kennethalamantia
'''
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "MovieTrailerSite",
    version = "1.0",
    packages = find_packages("src"),
    package_dir = {"" : "src"},
    include_package_data = True
)
