from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/blog/')
    def blog():
        return render_template('home.html')

    @app.route('/projects/')
    def projects():
        return 'hello'

    @app.route('/cv/')
    def cv():
        return render_template('home.html')

    return app