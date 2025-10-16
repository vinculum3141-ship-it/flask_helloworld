"""
This code defines a simple web application using Flask.
It creates a single route at the root URL ("/") that returns the message "Hello from Flask on Kubernetes (Minikube)!".
When run directly, it starts a web server listening on all network interfaces at port 5000.
This is typically used as a minimal example for deploying Flask apps, such as in a Kubernetes environment.
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on Kubernetes (Minikube)!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
