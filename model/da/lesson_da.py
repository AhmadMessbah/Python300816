from model.da.da import Da
from model.entity.lesson import Lesson


class LessonDa(Da):
    def save(self, lesson):
        self.connect()
        self.cursor.execute("INSERT INTO lesson_tbl(NAME, GRADE, TEACHER, START_DAY) VALUES(%s, %s, %s, %s)",
                            [lesson.name, lesson.grade, lesson.teacher, lesson.start_day])
        self.connection.commit()
        self.disconnect()

    def edit(self, lesson):
        self.connect()
        self.cursor.execute("UPDATE lesson_tbl SET NAME=%s, GRADE=%s, TEACHER=%s, START_DAY=%s WHERE ID=%s",
                            [lesson.name, lesson.grade, lesson.teacher, lesson.start_day, lesson.lesson_id])
        self.connection.commit()
        self.disconnect()

    def remove(self, lesson_id):
        self.connect()
        self.cursor.execute("DELETE FROM lesson_tbl WHERE ID=%s",
                            [lesson_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM lesson_tbl")
        lesson_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if lesson_tuple_list:
            lesson_list = []
            for lesson_tuple in lesson_tuple_list:
                lesson = Lesson(lesson_tuple[1], lesson_tuple[2], lesson_tuple[3], lesson_tuple[4])
                lesson.lesson_id = lesson_tuple[0]
                lesson_list.append(lesson)
            return lesson_list
        else:
            raise ValueError("No Lesson Found !")

    def find_by_id(self, lesson_id):
        self.connect()
        self.cursor.execute("SELECT * FROM lesson_tbl WHERE ID=%s", [lesson_id])
        lesson_tuple = self.cursor.fetchone()
        self.disconnect()
        if lesson_tuple:
            lesson = Lesson(lesson_tuple[1], lesson_tuple[2], lesson_tuple[3], lesson_tuple[4])
            lesson.lesson_id = lesson_tuple[0]
            return lesson
        else:
            raise ValueError("No lesson Found !")

    def find_by_name(self, name):
        self.connect()
        self.cursor.execute("SELECT * FROM lesson_tbl WHERE NAME=%s", [name])
        lesson_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if lesson_tuple_list:
            lesson_list = []
            for lesson_tuple in lesson_tuple_list:
                lesson = Lesson(lesson_tuple[1], lesson_tuple[2], lesson_tuple[3], lesson_tuple[4])
                lesson.person_id = lesson_tuple[0]
                lesson_list.append(lesson)
            return lesson_list
        else:
            raise ValueError("No Lesson Found !")

    def find_by_teacher(self, teacher):
        self.connect()
        self.cursor.execute("SELECT * FROM lesson_tbl WHERE TEACHER=%s", [teacher])
        lesson_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if lesson_tuple_list:
            lesson_list = []
            for lesson_tuple in lesson_tuple_list:
                lesson = Lesson(lesson_tuple[1], lesson_tuple[2], lesson_tuple[3], lesson_tuple[4])
                lesson.person_id = lesson_tuple[0]
                lesson_list.append(lesson)
            return lesson_list
        else:
            raise ValueError("No Lesson Found !")
