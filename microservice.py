from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import time
from prometheus_client import start_http_server, Gauge, Counter

# Метрики Prometheus
METRIC_HOST_TYPE = Gauge('host_type', 'Type of host (0=VM, 1=Container, 2=Physical)')
METRIC_REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        METRIC_REQUEST_COUNT.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def detect_host_type():
    # 0=VM, 1=Container, 2=Physical
    try:
        with open("/proc/1/cgroup", "r") as f:
            if "docker" in f.read() or "kubepods" in f.read():
                return 1  # Контейнер
    except:
        pass

    if "hypervisor" in open("/proc/cpuinfo").read().lower():
        return 0  # Виртуальная машина
    else:
        return 2  # Физический сервер

if __name__ == "__main__":
    # Определяем тип хоста и задаём метрику
    METRIC_HOST_TYPE.set(detect_host_type())
    
    # Запускаем Prometheus-метрики на порту 8080
    start_http_server(8080)
    
    # Запускаем HTTP-сервер (опционально)
    server = HTTPServer(('0.0.0.0', 8000), RequestHandler)
    print("Server running on http://0.0.0.0:8000")
    server.serve_forever()