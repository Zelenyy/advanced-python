from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
from string import Template

HTML_TEMPLATE = """<!DOCTYPE html>
<html>

<head>
    <title>Python</title>
</head>

<body>
<form action="post_handler.py", method="post">
   <input type="text">
   <input type="submit" value="Send Request"/>
</form>
</body>

</html>

"""


class Handler(BaseHTTPRequestHandler):

    def _header(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_HEAD(self):
        self._header()

    def do_GET(self):
        self._header()
        data = HTML_TEMPLATE
        data = bytes(data, "utf-8")
        self.wfile.write(data)

    def do_POST(self):
        pass


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=Handler)