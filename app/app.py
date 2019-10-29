from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route('/')
def home():
    return 'Welcome to the first commit!'
