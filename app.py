from flask import Flask
app = Flask(__name__)

print("Starting ..")

@app.route('/')
def hello_world():
    return 'Hello, gitpod test 2!'
