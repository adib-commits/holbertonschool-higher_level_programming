#!/usr/bin/python3
"""Simple API using Flask"""

from flask import Flask, jsonify, request


app = Flask(__name__)


users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route("/")
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """API status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return user information"""

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
