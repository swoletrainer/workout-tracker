from flask import Flask, request, render_template

app = Flask(__name__)   # Create application instance as a flask object

@app.route('/')
def index():
        return render_template('index.html')    # looks for file in templates dir
        
@app.route('/user/<name>')
def user(name):
        return render_template('user.html', name=name)    # looks for file in templates dir

@app.route('/agent')
def get_agent():
        user_agent = request.headers.get('User-Agent')
        return '<p>Your browser is {}!</p>'.format(user_agent)