#!/usr/bin/python3
"""API Security and Authentication using Flask"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials"""

    if username in users:
        if check_password_hash(
            users[username]["password"],
            password
        ):
            return username

    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected basic auth route"""

    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """Login and generate JWT token"""

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(
        users[username]["password"],
        password
    ):
        return jsonify({"error": "Invalid credentials"}), 401


    token = create_access_token(
        identity=username,
        additional_claims={
            "role": users[username]["role"]
        }
    )

    return jsonify({
        "access_token": token
    })


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """JWT protected route"""

    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin only route"""

    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({
            "error": "Admin access required"
        }), 403

    return "Admin Access: Granted"

@jwt.unauthorized_loader
def missing_token(error):
    return jsonify({
        "error": "Missing or invalid token"
    }), 401


@jwt.invalid_token_loader
def invalid_token(error):
    return jsonify({
        "error": "Invalid token"
    }), 401


@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({
        "error": "Token has expired"
    }), 401


if __name__ == "__main__":
    app.run()
