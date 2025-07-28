from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS = {"B.M.F COMEBACK": "Njogoma1960?"}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if USERS.get(username) == password:
        return jsonify({"success": True})
    return jsonify({"success": False}), 401

@app.route("/api/arbitrage", methods=["GET"])
def arbitrage():
    # Sample response
    return jsonify({
        "sport": "Football",
        "odds": {
            "Home": {"bookmaker": "Betika", "odd": 2.3},
            "Draw": {"bookmaker": "SportPesa", "odd": 3.4},
            "Away": {"bookmaker": "Odibets", "odd": 3.1}
        }
    })
