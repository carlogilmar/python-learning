from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print ("WebServer Ok")
    return 'Hello, Flask!'

@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hello</h1>, %s' % name

# following lines execute our app using the built-in development server in debug mode
if __name__ == '__main__':
    app.run(debug=True)

