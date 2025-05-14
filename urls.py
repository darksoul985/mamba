from views import *


routes = {
    "/": index_view,
    "/about/": About(),
    "/study-programm/": StudyProgramm(),
    "/courses-list/": CoursesList(),
    "/create-course/": CreateCourse(),
    "/category-list/": CategoryList(),
    "/create-category/": CreateCategory(),
}
