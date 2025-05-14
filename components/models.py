import quopri
from abc import ABC, abstractmethod
from typing import Literal, Optional


# класс - Абстрактный пользователь
class AbstractUser(ABC):
    def create(self, **kwargs):
        raise NotImplementedError


class BaseUser(AbstractUser):
    """Класс базового пользователя"""

    def __init__(
        self, username: str, fiers_name: str, last_name: str, email: str
    ) -> None:
        """
        Обязательные атрибуты всех пользователей
        """
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


class AbstractCategory(ABC):
    @abstractmethod
    def course_count(self) -> int:
        pass


class Category(AbstractCategory):
    auto_id = 0
    # _courses_list = []

    def __init__(self, name: str, category: Optional[AbstractCategory]):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self) -> int:
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
        return f"Course: {self.name} in the Category: {self.category}"


class InteractiveCource(BaseCourse):
    pass


class RecordCourse(BaseCourse):
    pass


class CourseFatory:
    types = {"interactive": InteractiveCource, "record": RecordCourse}

    @classmethod
    def create_course(cls, type_: str, name: str, category: Category):
        return cls.types[type_](name, category)
