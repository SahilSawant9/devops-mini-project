from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Majhe Naav Sahil Sawant"


# Only run the server if executed directly
if __name__ == '__main__':
    app.run()
