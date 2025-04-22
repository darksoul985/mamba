from views import *


routes = {
    '/': index_view,
    '/abc/': abc_view,
    '/other/': Other(),
    '/authors/': author_view,
}
