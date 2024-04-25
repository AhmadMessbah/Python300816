from model.entity.base import Base


class Lesson(Base):
    def __init__(self, name, grade, teacher, start_day):
        self.lesson_id = None
        self.name = name
        self.grade = grade
        self.teacher = teacher
        self.start_day = start_day

