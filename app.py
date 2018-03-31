from flask import Flask, render_template
from scripts.cinterest import compute_comp_int

app = Flask(__name__)


@app.route('/')
def index(): 
	return render_template ('INDEX.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__': 
	app.run(debug = True)