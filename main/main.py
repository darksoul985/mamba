from typing import Callable
from pprint import pprint
from views import not_found_404_view
from main.request_method import GetRequest, PostRequest


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
    
    
class Framework:
    def __init__(self, routes, *args):
        self.routes = routes
        # self.fronts = fronts
    
    def __call__(self, environ: dict, start_response: Callable):
        """
            environ (dict): словарь данных от сервера
            start_response (Callable): функция для ответа серверу
        """
        path = environ['PATH_INFO']
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        
        request = {}
        method = environ['REQUEST_METHOD']
        print(f'Method: {method}')
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Пришел GET запрос с параметрами: {request_params}')
        elif method == 'POST':
            request_params = PostRequest().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Пришел POST запрос с параметрами: {request_params}')

        # pprint(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]