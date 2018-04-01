from flask import Flask, render_template
from scripts.cinterest import compute_comp_int
from google.cloud import bigquery 
import json

app = Flask(__name__)


@app.route('/')
def index(): 
	return render_template ('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')


#Provie the user information on the stock that they are requesting information on 
@app.route('/stockUpdate',  methods=['POST']) 
def stockUpdate(): 
	return "you've reached stockUpdate"


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'



if __name__ == '__main__': 
	app.run(debug = True)