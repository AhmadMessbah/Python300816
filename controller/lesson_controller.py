from model.da.lesson_da import LessonDa
from model.da.person_da import PersonDa
from model.entity.lesson import Lesson
from model.tools.decorators import exception_handling



class LessonController:
    lesson_da = LessonDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, name, grade, date, teacher_id):
        if teacher_id:
            teacher = cls.person_da.find_by_id(teacher_id)
            lesson = Lesson(name, grade, date, teacher)
        else:
            lesson = Lesson(name, grade, date)

        cls.lesson_da.save(lesson)
        return True, f"Lesson saved successfully\n{lesson}"

    @classmethod
    @exception_handling
    def edit(cls, lesson_id, name, grade, date, teacher_id):
        teacher = cls.person_da.find_by_id(teacher_id)
        lesson = Lesson(name, grade, date, teacher)
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
    def find_by_name_for_teacher(cls, name, teacher_id):
        return True, cls.lesson_da.find_by_name_for_teacher(name, teacher_id)

    @classmethod
    @exception_handling
    def find_by_teacher(cls, teacher_id):
        return True, cls.lesson_da.find_by_teacher(teacher_id)

    @classmethod
    @exception_handling
    def find_teacher_count_by_teacher_id(cls, teacher_id):
        return True, cls.lesson_da.find_teacher_count_by_teacher_id(teacher_id)

