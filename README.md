Logs Analysis 

> Alan Grinberg

## About
In this project, we find a large database including over a million rows and pull out key data by leveraging SQL queries and connecting to the Python DB API. It is similar to an internal reporting tool that determines popularity of the authors and articles for a publication as well as tracking connections to the site. 

### Instructions

**Getting Ready**
To run the tool, please install or make sure you have Python 2, Vagrant, and VirtualBox. Install the necessary software and clone this repo.

**Running the tool**
Go into the Vagrant Virtual Machine by going to the directory vagrant on your machine and run `vagrant up` followed by a login with `vagrant ssh`.

To get the data set up, use `psql -d news -f newsdata.sql` to connect the database. 
To run the program, run CODE `python loganalysis.py` from the command line.


#### Notes
For any issues or comments, feel free to comment here or submit an issue.