# Github-Navigator
Using the Github API v3 , to create a web application to browse github repositories and find the ones corresponding to your serach_term.It then displaus the 5 last created ones.



Github Navigator :
=================

A simple WSGI application called GitHub navigator. It is able to search GitHub repositories by given search term and present them as an html page, sorted by creation date.

Features :
=========

1- Search GitHub Repository and fetches result using GitHub API and display result in basic format (using provided template)

2- The Homepage provides a Form to enter your search_term  http://localhost:9876

3- You can also directly access URL with the search_term and get the result http://localhost:9876/navigator?search_term=[search_term]

4- Search for the search_term in both the Title and description of the repository


usage scenario :
================

1- Install all the dependencies in 'dependencies.txt'.

2- Unzip and get into the 'assignment_solution' folder.

3- Start the application (`python application.py`).

4- Open a browser and do GET request to either one of those: 

		- http://localhost:9876/ 					==> acess a homepage with a Form to enter your search_term.
		
		- http://localhost:9876/navigator?search_term=[serach_term]     ==> for direct acess

By : Bendidi Ouail

11/11/2016.
