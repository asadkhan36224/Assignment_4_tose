from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ' asad has comeback!'


if __name__ == '__main__':
    app.run()
