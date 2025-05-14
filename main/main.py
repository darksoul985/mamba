from typing import Callable
from main.request_method import GetRequest, PostRequest
from views import PageNotFound404


class Framework:
    """Основной класс для запуска фреймворка"""

    def __init__(self, routes: dict[str, Callable], *args):
        """Принимает словарь путей с адресами"""
        self.routes = routes
        # self.fronts = fronts

    def __call__(self, environ: dict, start_response: Callable):
        """
        environ (dict): словарь данных от сервера
        start_response (Callable): функция для ответа серверу
        """
        path = environ["PATH_INFO"]
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        request = {}
        method = environ["REQUEST_METHOD"]
        request["method"] = method
        print(f"Method: {method}")
        if method == "GET":
            request_params = GetRequest().get_request_params(environ)
            request["request_params"] = request_params

        elif method == "POST":
            request_params = PostRequest().get_request_params(environ)
            request["data"] = request_params

        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
