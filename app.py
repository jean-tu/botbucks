from flask import Flask, jsonify, request
from flask import render_template
from flask import request, make_response # in order to be able to use the webhook
#from scripts.cinterest import compute_comp_int
#from google.cloud import bigquery
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/stockticker', methods=['POST'])
def receiveStockTicker():
    stock_ticker = {'stock' : request.json["outputContexts"]}
    print(stock_ticker)

@app.route('/disgraph')
def dis_graph():
    return render_template('disgraph.html')

@app.route('/twxgraph')
def twx_graph():
    return render_template('twxgraph.html')

@app.route('/viacomgraph')
def viacom_graph():
    return render_template('viacomgraph.html')

#Provide the user information on the stock that they are requesting information on
@app.route('/compute', methods=['POST'])
def compute():
    print("HELLO INSIDE COMPUTE") #debug
    coffeeprice = "This is a response from GAE !!!"
    my_response = {
	   "speech": "hello",
       "diaplayText": "hello", 
    }
    res = json.dump(my_response)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'



if __name__ == '__main__':
	app.run(debug = True)
