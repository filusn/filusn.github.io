from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/projects/')
    def projects():
        projects = [
            {
                'title': 'ML fine art price prediction',
                'body': 'Check if ML can predict the price of paintings.'
            },
            {
                'title': 'Confocal microscopy',
                'body': 'Tumour cell detection on confocal microscopy images'
            },
            {
                'title': 'Deutsch Meister',
                'body': 'Python and Starlette based app helping me and my friends to follow and repeat what have we learned.'
            },
            {
                'title': 'QuantX Backtest',
                'body': 'Backtesting engine for stock market.'
            },
            {
                'title': 'Jigsaw Puzzle Solver',
                'body': 'AI approach for solving jigsaw puzzles.'
            }
        ]
        return render_template('projects.html', projects=projects)

    @app.route('/blog/')
    def blog():
        posts = [
            {
                'title': 'pytest mini tutorial',
                'date': '1.11.2019',
                'body': 'This is mini pytest tutorial'
            },
            {
                'title': 'ML Conference',
                'date': '29.09.2019',
                'body': 'I was on a conference...'
            },
            {
                'title': 'HackYeah',
                'date': '10.10.2019',
                'body': 'Events on HackYeah...'
            }
        ]
        return render_template('blog.html', posts=posts)

    @app.route('/cv/')
    def cv():
        return render_template('cv.html')

    return app
