from flask import Flask, render_template
from scripts.cinterest import compute_comp_int

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

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__': 
	app.run(debug = True)