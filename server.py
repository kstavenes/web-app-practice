from flask import Flask

# This defines the variable app as a Flask application instance
app = Flask(__name__)


# This is a decorator. This particular decorator tells our
# Flask app to assign the function that it precedes to
# the '/' or 'root' URL.
@app.route('/', methods=['GET'])
def home():
    # This is what the browser will render in plain text
    return '<p>Hello World!</p>'


@app.route('/foo', methods=['GET'])
def foo():
    return 'Not found here'


@app.route('/sum/<int:x>/<int:y>', methods=['GET'])
def add(x, y):
    return str(x + y)

# Basically, "if we're not being imported as a module
# execute the app.run() method, else do nothing"
# This is useful when you want to reuse some functionality
# in another application, but don't want to run THIS module
# as an application: Behavior vs Features
if __name__ == '__main__':
    # Setting "debug=True" gives us some
    # extra output that we can interact with
    # in case of an error / exception.
    app.run(debug=True)
