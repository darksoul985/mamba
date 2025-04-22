from abc import ABC, abstractmethod


class AbstractRequest(ABC):
    @abstractmethod
    def get_request_params(self, environ: dict):
        """Метод для получения параметров запроса

        Args:
            environ (dict): словарь с переменными запроса
        """
        raise NotImplementedError


class BaseRequest(AbstractRequest):
    def parse_input_data(self, data: str) -> dict:
        """Преобразование строки в словарь с параметрами запроса

        Args:
            data (str): строка с параметрами запросов

        Returns:
            dict: словарь с параметрами запроса
        """
        result = {}
        if data:
            params = data.split("&")
            for param in params:
                k, v = param.split("=")
                result[k] = v
        return result


class GetRequest(BaseRequest):
    def get_request_params(self, environ: dict) -> dict:
        quety_string = environ["QUERY_STRING"]
        request_params = GetRequest().parse_input_data(quety_string)
        return request_params


class PostRequest(BaseRequest):
    def get_request_params(self, environ):
        content_length_data: bytes = environ.get("CONTENT_LENGTH")

        content_length = int(content_length_data) if content_length_data else 0
        data = (
            environ.get("wsgi.input").read(content_length)
            if content_length > 0
            else b""
        )
        result = {}
        if data:
            data_str = data.decode(encoding="utf-8")
            result = PostRequest().parse_input_data(data_str)
        return result
