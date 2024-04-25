from model.da.lesson_da import LessonDa
from model.entity.lesson import Lesson
from model.tools.validator import Validator


class PersonController:
    def __init__(self):
        self.validator = Validator()

    def save(self, name, grade, teacher, year, month, day):
        try:
            lesson = Lesson(
                self.validator.name_validator(name, "Invalid Name"),
                self.validator.grade_validator(grade, "Invalid Grade"),
                self.validator.name_validator(teacher, "Invalid Teacher Name"),
                self.validator.date_validator(year, month, day, "Invalid Date")
            )
            lesson_da = LessonDa()
            lesson_da.save(lesson)
            return True, f"Person saved successfully\n{lesson}"
        except Exception as e:
            return False, str(e)

    def edit(self, lesson_id, name, grade, teacher, year, month, day):
        try:
            lesson = Lesson(
                self.validator.name_validator(name, "Invalid Name"),
                self.validator.grade_validator(grade, "Invalid Grade"),
                self.validator.name_validator(teacher, "Invalid Teacher Name"),
                self.validator.date_validator(year, month, day, "Invalid Date")
            )
            lesson = Lesson(name, grade, teacher, start_day) //TODO درسته؟
            lesson.lesson_id = lesson_id
            lesson_da = LessonDa()
            old_lesson = lesson_da.find_by_id(lesson_id)
            lesson_da.edit(lesson_id)
            return True, (f"Lesson edited successfully\nFrom : {old_lesson}\nTo: {lesson}")
        except Exception as e:
            return False, str(e)

    def remove(self, lesson_id):
        try:
            lesson_da = LessonDa()
            lesson = lesson_da.find_by_id(lesson_da)
            lesson_da.remove(lesson_id)
            return True, f"Lesson removed successfully\n{lesson}"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            lesson_da = LessonDa()
            return True, lesson_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, lesson_id):
        try:
            lesson_da = LessonDa()
            return True, lesson_da.find_by_id(lesson_id)
        except Exception as e:
            return False, str(e)

    def find_by_name(self, name):
        try:
            lesson_da = LessonDa()
            return True, lesson_da.find_by_name(
                self.validator.name_validator(name, "Invalid Name")
            )
        except Exception as e:
            return False, str(e)

    def find_by_teacher(self, teacher):
        try:
            lesson_da = LessonDa()
            return True, lesson_da.find_by_teacher(
                self.validator.name_validator(teacher, "Invalid Teacher Name")
            )
        except Exception as e:
            return False, str(e)
