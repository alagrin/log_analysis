# Logs Analysis 

> Alan Grinberg

## About
In this project, we find a large database including over a million rows and pull out key data by leveraging SQL queries and connecting to the Python DB API. It is similar to an internal reporting tool that determines popularity of the authors and articles for a publication as well as tracking connections to the site. 

Key Questions answered in this project... What are the top 3 viewed articles in the database,who are the top article authors who's works have been viewed, and what days had more than 1% of requests to the site end in errors.

### Instructions

**Getting Ready**
To run the tool, please install or make sure you have Python 2, Vagrant, and VirtualBox. Install the necessary software and clone this repo. Here are some download links:
[Vagrant](https://www.vagrantup.com/downloads.html),
[VirtualBox](https://www.virtualbox.org/wiki/Downloads)

**Running the tool**
Go into the Vagrant Virtual Machine (Vagrantfile configuration included in repo) by going to the directory vagrant on your machine and run `vagrant up` followed by a login with `vagrant ssh`.

To get the data set up, first download this [zip file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file to extract `newsdata.sql` and use command `psql -d news -f newsdata.sql` to connect the database. 
To run the program, run CODE `python loganalysis.py` from the command line.


#### Notes
For any issues or comments, feel free to comment here or submit an issue.