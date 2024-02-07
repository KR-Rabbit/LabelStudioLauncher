import contextlib
import socket
from http.server import SimpleHTTPRequestHandler
from http.server import ThreadingHTTPServer

from PySide6.QtCore import QThread, Signal


def _get_best_family(*address):
    infos = socket.getaddrinfo(
        *address,
        type=socket.SOCK_STREAM,
        flags=socket.AI_PASSIVE,
    )
    family, type_, proto, canon_name, sock_addr = next(iter(infos))
    return family, sock_addr


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
    started_signal = Signal(str)

    def __init__(self, ip="::", port=8000, directory="./"):
        super().__init__()
        self.directory = directory
        # 目录为directory的HTTP服务器
        try:
            server_class = DualStackServer
            server_class.address_family, addr = _get_best_family(ip, port)
            self.server = server_class(addr, CORSRequestHandler)
            self.server.directory = directory
        except socket.error:
            self.server = None
            raise OSError(f"启动HTTP服务失败 {ip}:{port}")

    def run(self):
        # 返回启动的地址,通过socket获取
        # ip=localhost,就显示localhost
        # 如果全部监听,就显示本机ip
        if self.server.server_address[0] == "::":
            ip = socket.gethostbyname(socket.gethostname())
        else:
            ip = "localhost"
        port = self.server.server_address[1]
        self.started_signal.emit(f"http://{ip}:{port}")

        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
