from .models import *


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_: Literal["student", "teacher"]) -> BaseUser:
        return UserFactory.create(type_)

    @staticmethod
    def create_category(
        name: str,
        category: AbstractCategory | None = None,
    ) -> Category:
        return Category(name, category)

    def find_category_by_id(self, id: int):
        for item in self.categories:
            print("Engine find_category_by_id item", item.id)
            if item.id == id:
                return item
        raise ValueError(f"Нет категории с id: {id}")

    @staticmethod
    def crate_course(
        type_: Literal["record", "interactive"], name: str, category: Category
    ):
        return CourseFatory.create_course(type_, name, category)

    def get_course_by_name(self, name: str):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace("%", "=").replace("+", " "), "UTF-8")
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode("UTF-8")
