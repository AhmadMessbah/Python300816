from model.da.lesson_da import LessonDa
from model.entity.lesson import Lesson
from model.tools.decorators import exception_handling
from model.tools.validator import Validator


class LessonController:
    lesson_da = LessonDa()

    @classmethod
    @exception_handling
    def save(cls, name, grade, teacher, year, month, day):
        lesson = Lesson(name, grade, teacher, (year, month, day))
        cls.lesson_da.save(lesson)
        return True, f"Lesson saved successfully\n{lesson}"

    @classmethod
    @exception_handling
    def edit(cls, lesson_id, name, grade, teacher, year, month, day):
        lesson = Lesson(name, grade, teacher, (year, month, day))
        lesson.lesson_id = lesson_id
        old_lesson = cls.lesson_da.find_by_id(lesson_id)
        cls.lesson_da.edit(lesson)
        return True, f"Lesson edited successfully\nFrom : {old_lesson}\nTo: {lesson}"

    @classmethod
    @exception_handling
    def remove(cls, lesson_id):
        lesson = cls.lesson_da.find_by_id(lesson_id)
        cls.lesson_da.remove(lesson_id)
        return True, f"Lesson removed successfully\n{lesson}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.lesson_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, lesson_id):
        return True, cls.lesson_da.find_by_id(lesson_id)

    @classmethod
    @exception_handling
    def find_by_name(cls, name):
        return True, cls.lesson_da.find_by_name(name)

    @classmethod
    @exception_handling
    def find_by_teacher(cls, teacher):
        return True, cls.lesson_da.find_by_teacher(teacher)
