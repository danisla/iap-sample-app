from http.server import HTTPServer, BaseHTTPRequestHandler
import os
PORT = int(os.environ.get("PORT", "8080"))
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("""
        <!doctype html><html>
    <head><title>ESP Sample App</title><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"></head>
    <body>
    <div class="container">
    <div class="row">
    <div class="col s2">&nbsp;</div>
    <div class="col s8">
    <div class="card blue">
        <div class="card-content white-text">
            <h4>Hello %s</h4>
        </div>
        <div class="card-action">
            <a href="/_gcp_iap/identity">Identity JSON</a>
            <a href="/_gcp_iap/clear_login_cookie">Logout</a>
        </div>
    </div></div></div></div>
    </body></html>
        """ % self.headers.get("x-goog-authenticated-user-email","unauthenticated user").split(':')[-1], "utf8"))
print("Listing on port", PORT)
server = HTTPServer(('0.0.0.0', PORT), RequestHandler)
server.serve_forever()
