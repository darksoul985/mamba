import quopri
from abc import ABC


# класс - Абстрактный пользователь
class AbstractUser(ABC):
    def create(self, **kwargs):
        raise NotImplementedError


class BaseUser(AbstractUser):
    id = 0

    def __init__(self, username, fiers_name, last_name, email):
        self.username = username
        self.fiers_name = fiers_name
        self.last_name = last_name
        self.email = email


class Teacher(BaseUser):
    def create(self, **kwargs):
        for key, val in kwargs.items():
            self.__dict__[key] = val


class Student(BaseUser):
    def create(self, **kwargs):
        for key, val in kwargs.items():
            self.__dict__[key] = val


# класс - Фабрика пользователей
class UserFactory:
    types = {"student": Student, "teacher": Teacher}

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class Category:
    auto_id = 0
    # _courses_list = []

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result

    def __repr__(self):
        return f"Category: {self.name}"


class BaseCourse:
    def __init__(self, name: str, category: Category):
        self.name = name
        self.category = category
        self.category.courses.append(self)

    def __repr__(self):
        return f"Curse: {self.name} - {self.category}"


class ProgrammingCourse(BaseCourse):
    pass


class HistoryCourse(BaseCourse):
    pass


class CourseFatory(BaseCourse):
    type_ = {"programming": ProgrammingCourse, "history": HistoryCourse}

    @staticmethod
    def create_course(cls, type_, name, category=None):
        return cls.typs


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_: str) -> BaseUser:
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name: str, category: str | None = None) -> Category:
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print("item", item.id)
            if item.id == id:
                return item
        raise ValueError(f"Нет категории с id: {id}")

    @staticmethod
    def crate_course(type_, name, category):
        return CourseFatory.create_course(type_, name, category)

    def get_courses(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace("%", "=").replace("+", " "), "UTF-8")
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode("UTF-8")
