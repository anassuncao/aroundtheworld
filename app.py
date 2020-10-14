import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Does it work?'

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    #DO NOT FORGET TO SET THIS TO FALSE IN THE END OF THE PROJECT

