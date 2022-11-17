from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
import plotly.express as px
import io


df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

class Handler(BaseHTTPRequestHandler):

    def _header(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_HEAD(self):
        self._header()

    def do_GET(self):
        self._header()
        buffer = io.StringIO()
        fig.write_html(buffer)
        data= bytes(buffer.getvalue(), "utf-8")
        self.wfile.write(data)




def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=Handler)