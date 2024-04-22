from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey this is my first flask project i initialized'

if __name__ == '__main__':
    app.run(debug=True)
