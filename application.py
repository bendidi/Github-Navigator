## import necessary python libraries

from flask import Flask, render_template, request 			
import requests as requests 						
import json

 #creating an instance of the Flask class
app = Flask(__name__)

 # We tell Flask what URL should trigger our index function
@app.route("/")
def index():
	# render the template 'templates/indice.html', containing the basic interface where users can input their search_term  				  
	return render_template('index.html')  

@app.route("/navigator") # The URL that triggers the navigator function
def navigator():
	search_term=request.args.get('search_term', '')  #GET the input argument (search_term)
	r = requests.get("https://api.github.com/search/repositories?q="+search_term) #send request to the github API to search for repositories
		#The term search is done in the Tilte and description of the repo, and returns the first page of found repos.
	data=r.json() #Parse data into a python dictionary
	total = data['total_count'] #Total number of found repositories in page1
	if total == 0 :
		return "No repositories found coresponding to your search_term.Try again using a different search term."
	top5 = sorted(data['items'], key=lambda d: d['created_at'],reverse=True)[0:5] #Get the top 5 repositories classified by creation date
	#process data , and create commit keys for the top5 repositories
	for x in top5:
		x['created_at']=x['created_at'][0:10]+' '+x['created_at'][11:19]
		comit = requests.get(x['commits_url'][0:-6])
		comit_data=comit.json()
		x['Xsha']= comit_data[0]['sha']
		x['XMessage']=comit_data[0]['commit']['message']
		x['Xname']=comit_data[0]['commit']['committer']['name']

	return render_template(
        	'template.html', **locals()) #render the template 'templates/template.html'
if __name__ == "__main__":
    app.run(host='localhost', port=9876) #run the app on localhost, and port 9876








