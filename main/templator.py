from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name: str, template_folder="templates", **kwargs) -> str:
    """минимальный пример работы с шаблонизатором

    Args:
        template_name (str): имя шаблона
    """
    env = Environment()
    # указываем папку для поиска шаблонов
    env.loader = FileSystemLoader(template_folder)
    # находим шаблон в окружении
    template = env.get_template(template_name)

    return template.render(**kwargs)
