from flask import Flask, render_template


# Create a flask instance

app = Flask(__name__)


# Create a route decorator

@app.route("/")
def index():
    return render_template('index.html')

# Users page

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


# Custom errors page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500