from main.templator import render


# page controller
def index_view(request):
    return "200 OK", render("index.html")


def abc_view(request):
    return "200 OK", "ABC"


def author_view(request):
    objects = [
        {"name": "Карл Маркс"},
        {"name": "Фридрих Энгельс"},
        {"name": "Надежда Крупская"},
    ]
    return "200 OK", render("authors.html", object_list=objects)


def not_found_404_view(request):
    return "404 WHAT", [b"404 PAGE Not Found"]


class Other:
    def __call__(self, request):
        return "200 OK", ["<h1>Что то другое</h2>".encode("utf-8")]

