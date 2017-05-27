import os
import logging
from flask import Flask

app = Flask(__name__)
logging.basicCongig(level=logging.DEBUG)

@app.route('/')
def hello():
		logging.debug("saying hello")
		return 'Hello EventApp!'

if __name__ == "__main__":
	app.run()