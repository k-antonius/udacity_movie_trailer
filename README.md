#------------------------------#
#			       #
# Simple Movie Trailer Website #
# 	       	       	       #
#------------------------------#

Introduction:

This is a simple python package that loads a movie trailer website in the
default browser. You can change the movies that are loaded by editing
"movie_data.csv" in the src/movie_trailer_site/data/ directory.

Installation:

For the source code, fork the repository and then clone.

To install the package, open your shell of choice, navigate to the download
directory and run "python setup.py install" which will intall the package on
your PYTHONPATH.

If your python installation does not have the setuptools package, it will be
installed, which requires an active network connection. See below for details.

    # Dependencies: The setuptools package for installation.
      		    The pkg_resources package for its ResourceManager API.
		    pkg_resources is packaged with setuptools.

Running It:

Open your shell and start the python interpreter in interactive mode. From the
movie_trailer_site package import movie_server. Run the load_movie_trailer_site
function. The website should load in your brower.

This package has been tested on macOS 10.12, Windows 10, and Ubuntu 16.10. It
has been tested both in firefox and chrome.

Uninstalling:

Remove the package from your python site-base directory. Remove the download
from the location you saved it to.