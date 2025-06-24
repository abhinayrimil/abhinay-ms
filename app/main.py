from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)
REQUEST_COUNT = Counter("app_requests_total", "Total HTTP requests")

@app.route("/")
def index():
    REQUEST_COUNT.inc()
    return "Hello from abhinay-ms!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080 )
