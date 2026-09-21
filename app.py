from http.server import BaseHTTPRequestHandler, HTTPServer


class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = """
        <html>
            <head>
                <title>Greeter App</title>
            </head>
            <body>
                <h1>Hi, Talha!</h1>
                <p>Welcome to my containerized Python application.</p>
                <p>Learning Git and Docker!</p>
            </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8000), GreeterHandler)

print("Greeter app running on http://localhost:8000")

server.serve_forever()