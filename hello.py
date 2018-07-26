from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)   # Create application instance as a flask object
bootstrap = Bootstrap(app)
moment = Moment(app)

# These are view functions
@app.route('/')
def index():
        return render_template('index.html', current_time=datetime.utcnow())    # looks for file in templates dir

        
@app.route('/user/<name>')
def user(name):
        return render_template('user.html', name=name)    # looks for file in templates dir

@app.route('/agent')
def get_agent():
        user_agent = request.headers.get('User-Agent')
        return '<p>Your browser is {}!</p>'.format(user_agent)

# handling error codes 
@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
        return render_template('500.html')