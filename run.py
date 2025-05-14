# !/usr/bin/env python3
#  -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from main.main import Framework
from urls import routes


def main():
    application = Framework(routes)
    with make_server("", port=5555, app=application) as httpd:
        host, port = httpd.server_address
        match host:
            case "0.0.0.0":
                host = "//localhost"
        print(f"Serving on port http:{host}:{port}...")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
