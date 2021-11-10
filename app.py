from flask import Flask

app= Flask(__name__)

@app.route("/")
def get_index():
    return "Hello from Flask"