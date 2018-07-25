from flask import Flask

app = Flask(__name__)   # Create application instance as a flask object

@app.route('/')
def index():
        return '<h1>Workout Tracker</h1>'

@app.route('/user/<name>')
def user(name):
        return '<h1>Hello, {}!</h1>'.format(name)