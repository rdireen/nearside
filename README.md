
[![Build status](https://ci.appveyor.com/api/projects/status/ccwuv424wao4rbly?svg=true)](https://ci.appveyor.com/project/rdireen/nearside)
[![Build Status](https://travis-ci.org/rdireen/nearside.svg?branch=master)](https://travis-ci.org/rdireen/nearside) 
[![Coverage Status](https://coveralls.io/repos/rdireen/nearside/badge.svg?branch=master)](https://coveralls.io/r/rdireen/nearside?branch=master)

NearSide
========
Description: a package for processing antenna near-field data.

Install
=======

**Ubuntu:**

NearSide uses NumPy so you need to decide if you want to build it yourself with

    $ sudo pip install numpy

or download the package with

    $ sudo apt-get install python-numpy

I have been building NumPy using the pip method, but it takes a long time. 

Once you have NumPy, install NearSide with 

    $ sudo pip install nearside 
    
**Windows:**
Make sure you have Numpy on your machine (I recommend using Anaconda), then

    $ pip install nearside 

Credits
=======
The algorithms within this package have been implemented, in part, using the documentation within 
the NIST Interagency/Internal Report (NISTIR) - 3955 [citation](http://www.nist.gov/manuscript-publication-search.cfm?pub_id=1051).
The majority or the code, however, has been developed using Ronald C. Wittmann's unpublished notes.


Contributing
============
Reporting bugs, suggesting features, helping with documentation, and adding to the code is very welcome. See
[Contributing](CONTRIBUTING.md). 

License
=======

Copyright (C) 2015  Randy Direen <nearside@direentech.com>.
NearSide is licensed under GNU General Public License, version 3, a copy of this license has been provided within the COPYING file in this directory, and can also be found at <http://www.gnu.org/licenses/>.
 
