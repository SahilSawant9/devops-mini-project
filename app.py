from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Sahil Sawant'  # Only your name now


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
