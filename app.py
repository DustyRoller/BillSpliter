from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.cfg")

if __name__ == '__main__':
    from routes import *
    app.run(debug=True)