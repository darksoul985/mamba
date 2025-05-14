from components.engine import Engine
from main.templator import render
from pprint import pprint
from datetime import date


site = Engine()


# page controller
def index_view(request):
    return "200 OK", render("index.html", objects_list=site.categories)


class About:
    """Страница о нас"""

    def __call__(self, request):
        return "200 OK", render("about.html")


class CoursesList:
    """Список курсов определенной категории"""

    def __call__(self, request):
        try:
            category = site.find_category_by_id(int(request["request_params"]["id"]))
            return "200 OK", render(
                "course_list.html",
                objects_list=category.courses,
                name=category.name,
                id=category.id,
            )
        except KeyError:
            return "200 OK", "No courses have been added yet"


class CreateCourse:
    """Создать курс для заданной категории"""

    category_id = -1

    def __call__(self, request):
        if request["method"] == "POST":
            data = request["data"]["name"]
            name = site.decode_value(data)
            category = None
            print(self.__dict__)
            if self.category_id != -1:
                print(
                    f"Передана категория CreateCourse с category_id: {self.category_id}"
                )
                category = site.find_category_by_id(int(self.category_id))
                course = site.crate_course("record", name, category)
                site.courses.append(course)

            return "200 OK", render(
                "course_list.html",
                objects_list=category.courses,
                name=category.name,
                id=category.id,
            )
        else:
            try:
                self.category_id = int(request["request_params"]["id"])
                pprint(f"Передана категория CreateCourse по else с id: {request}")
                category = site.find_category_by_id(self.category_id)
                return "200 OK", render(
                    "create_course.html",
                    name=category.name,
                    id=category.id,
                )
            except KeyError:
                return "200 OK", "No categories have been added yet!"


class CategoryList:
    """Список категорий"""

    def __call__(self, request):
        return "200 OK", render("category_list.html", objects_list=site.categories)


class CreateCategory:
    """Созадать категорию"""

    def __call__(self, request):
        if request["method"] == "POST":
            pprint(f"Состав POST CreateCategory: {request}")
            data = request["data"]
            name = site.decode_value(data["name"])
            category_id = data.get("category_id")
            category = None

            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return "200 OK", render("index.html", objects_list=site.categories)
        else:
            categories = site.categories
            return "200 OK", render(
                "create_category.html",
                categories=categories,
            )


class PageNotFound404:
    """Ошибка, страница не найдена"""

    def __call__(self, request):
        return "404 WHAT", "404 PAGE Not Found"


class StudyProgramm:
    """Страница расписания"""

    def __call__(self, request):
        return "200 OK", render("study_programs.html", date=date.today())
