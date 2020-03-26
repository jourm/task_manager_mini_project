from flask import Flask
import os
from os import path
if path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World...... again"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
