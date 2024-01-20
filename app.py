from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Community Garden Optimizer!'

if __name__ == '__main__':
    app.run(port=5002)  # Use a different port, e.g., 5002
