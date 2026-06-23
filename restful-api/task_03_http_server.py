#!/usr/bin/python3
"""Simple API using http.server"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIHandler(BaseHTTPRequestHandler):
    """Handle API requests"""

    def do_GET(self):
        """Handle GET requests"""

        if self.path == "/":
            response = "Hello, this is a simple API!"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(response.encode("utf-8"))

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            response = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(response.encode("utf-8"))

        elif self.path == "/status":
            response = "OK"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(response.encode("utf-8"))

        elif self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            response = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(response.encode("utf-8"))

        else:
            response = "Endpoint not found"

            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(response.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=APIHandler, port=8000):
    """Start HTTP server"""

    server_address = ("", port)

    httpd = server_class(server_address, handler_class)

    print("Server running on port {port}")

    httpd.serve_forever()


if __name__ == "__main__":
    run()
