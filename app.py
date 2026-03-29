from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK, API çalışıyor!")

def run():
    server_address = ('', 8000)  # Portu 8000 olarak ayarlıyoruz
    httpd = HTTPServer(server_address, Handler)
    print("Sunucu çalışıyor...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
