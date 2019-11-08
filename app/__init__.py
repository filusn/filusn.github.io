from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def home():
        return render_template('home.html',header='About me')

    @app.route('/projects/')
    def projects():
        projects = [
            {
                'title': 'ML fine art price prediction',
                'body': 'Check if ML can predict the price of paintings.',
                'url': 'fine_art'
            },
            {
                'title': 'Confocal microscopy',
                'body': 'Tumour cell detection on confocal microscopy images',
                'url': 'confocal_microscopy'
            },
            {
                'title': 'Deutsch Meister',
                'body': 'Python and Starlette based app helping me and my friends to follow and repeat what have we learned.',
                'url': 'deutsch_meister'
            },
            {
                'title': 'QuantX Backtest',
                'body': 'Backtesting engine for stock market.',
                'url': 'quantx_backtest'
            },
            {
                'title': 'Jigsaw Puzzle Solver',
                'body': 'AI approach for solving jigsaw puzzles.',
                'url': 'jigsaw_puzzle_solver'
            }
        ]
        return render_template('projects.html', projects=projects)

    @app.route('/blog/')
    def blog():
        posts = [
            {
                'title': 'pytest mini tutorial',
                'date': '1.11.2019',
                'body': 'This is mini pytest tutorial',
                'url': 'pytest_mini_tutorial'
            },
            {
                'title': 'ML Conference',
                'date': '29.09.2019',
                'body': 'I was on a conference...',
                'url': 'ml_conference'
            },
            {
                'title': 'HackYeah',
                'date': '10.10.2019',
                'body': 'Events on HackYeah...',
                'url': 'hackyeah2019'
            }
        ]
        return render_template('blog.html', posts=posts)

    @app.route('/cv/')
    def cv():
        return render_template('cv.html')

    @app.route('/projects/<project_url>/')
    def project_page(project_url):
        return render_template(f'projects/{project_url}.html')

    @app.route('/blog/<post_url>/')
    def blog_page(post_url):
        return render_template(f'posts/{post_url}.html')

    @app.errorhandler(404)
    def not_found(exc):
        return 'Not found 404'

    return app
