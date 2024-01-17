import contextlib
import signal
import socket
from http.server import HTTPServer, ThreadingHTTPServer
from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler

from PySide6.QtCore import QThread


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        SimpleHTTPRequestHandler.end_headers(self)


class DualStackServer(ThreadingHTTPServer):

    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(
                socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self,
                                 directory=self.directory)


class CORS_HTTPServer(QThread):
    def __init__(self, ip="0.0.0.0", port=8000, directory="./"):
        super().__init__()
        self.directory = directory
        # 目录为directory的HTTP服务器
        self.server = DualStackServer((ip, port), CORSRequestHandler)
        self.server.directory = directory

    def run(self):
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
