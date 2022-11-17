import time
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from string import Template

HTML_TEMPLATE = Template("""<!DOCTYPE html>
<html>
  
<head>
    <title>Page Title</title>
    <meta http-equiv="refresh" content="1">
</head>
  
<body>
    ${body}
</body>
  
</html>

""")

def counter_generator():
    counter = 0
    while True:
        yield counter
        counter +=1

class Handler(BaseHTTPRequestHandler):

    counter = counter_generator()

    def _header(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_HEAD(self):
        self._header()

    def do_GET(self):
        self._header()
        data = "<h1>" + str(next(self.counter)) + "</h1>\n"
        data = HTML_TEMPLATE.substitute({"body": data})
        data = bytes(data, "utf-8")
        self.wfile.write(data)





def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=Handler)