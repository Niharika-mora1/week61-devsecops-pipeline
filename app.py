from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Week 61 DevSecOps Project",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
