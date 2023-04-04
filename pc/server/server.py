from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import cgi

class RequestsHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("User-Agent","sample")
        self.end_headers()
        html = "OK"
        self.wfile.write(html.encode())

        # POST されたフォームデータを解析する
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        # HTTP Clientから「value=%s」の値を送信している為、form["value"].valueで値を取得する
        print(form["value"].value)

        return

ip = '0.0.0.0'
port = 8000

server = HTTPServer((ip, port), RequestsHandler)
print("Serving HTTP on "+ip+" port "+str(port)+" (http://"+ip+":"+str(8000)+"/)")
server.serve_forever()
