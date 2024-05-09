from model.da.da import Da
from model.da.person_da import PersonDa
from model.entity.lesson import Lesson


class LessonDa(Da):
    def save(self, lesson):
        if (lesson.teacher and self.find_teacher_count_by_teacher_id(lesson.teacher.person_id) < 10):
            self.connect()
            self.cursor.execute("INSERT INTO LESSON_TBL(NAME, GRADE, START_DAY, TEACHER_ID) VALUES(%s, %s, %s, %s)",
                                [lesson.name, lesson.grade, lesson.start_day, lesson.teacher.person_id])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Teacher Or Cant Save Any More !!!")

    def edit(self, lesson):
        if (lesson.teacher and self.find_teacher_count_by_teacher_id(lesson.teacher.person_id) < 10):
            self.connect()
            self.cursor.execute("UPDATE LESSON_TBL SET NAME=%s, GRADE=%s, START_DAY=%s, TEACHER_ID=%s WHERE ID=%s",
                                [lesson.name, lesson.grade, lesson.start_day, lesson.teacher.person_id, lesson.lesson_id])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Teacher Or Cant Save Any More !!!")

    def remove(self, lesson_id):
        self.connect()
        self.cursor.execute("DELETE FROM LESSON_TBL WHERE ID=%s",
                            [lesson_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM LESSON_TBL")
        lesson_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if lesson_tuple_list:
            lesson_list = []
            for lesson_tuple in lesson_tuple_list:
                lesson = Lesson(lesson_tuple[1],
                                lesson_tuple[2],
                                lesson_tuple[3],
                                person_da.find_by_id(lesson_tuple[4]))
                lesson.lesson_id = lesson_tuple[0]
                lesson_list.append(lesson)
            return lesson_list
        else:
            raise ValueError("No Lesson Found !")

    def find_by_id(self, lesson_id):
        self.connect()
        self.cursor.execute("SELECT * FROM LESSON_TBL WHERE ID=%s", [lesson_id])
        lesson_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if lesson_tuple:
            lesson = Lesson(lesson_tuple[1],
                            lesson_tuple[2],
                            lesson_tuple[3],
                            person_da.find_by_id(lesson_tuple[4]))
            lesson.lesson_id = lesson_tuple[0]
            return lesson
        else:
            raise ValueError("No lesson Found !")

    def find_by_name(self, name):
        self.connect()
        self.cursor.execute("SELECT * FROM LESSON_TBL WHERE NAME LIKE %s", [name + "%"])
        lesson_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if lesson_tuple_list:
            lesson_list = []
            for lesson_tuple in lesson_tuple_list:
                lesson = Lesson(lesson_tuple[1],
                                lesson_tuple[2],
                                lesson_tuple[3],
                                person_da.find_by_id(lesson_tuple[4]))
                lesson.lesson_id = lesson_tuple[0]
                lesson_list.append(lesson)
            return lesson_list
        else:
            raise ValueError("No Lesson Found !")

    def find_by_teacher(self, teacher_id):
        self.connect()
        self.cursor.execute("SELECT * FROM LESSON_TBL WHERE TEACHER_ID LIKE %s", [teacher_id + "%"])
        lesson_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if lesson_tuple_list:
            lesson_list = []
            for lesson_tuple in lesson_tuple_list:
                lesson = Lesson(lesson_tuple[1],
                                lesson_tuple[2],
                                lesson_tuple[3],
                                person_da.find_by_id(lesson_tuple[4]))
                lesson.lesson_id = lesson_tuple[0]
                lesson_list.append(lesson)
            return lesson_list
        else:
            raise ValueError("No Lesson Found !")

    def find_teacher_count_by_teacher_id(self, teacher_id):
        self.connect()
        self.cursor.execute("SELECT COUNT(TEACHER_ID) FROM LESSON_TBL WHERE TEACHER_ID=%s", [teacher_id])
        lesson = self.cursor.fetchone()
        self.disconnect()
        if lesson:
            return int(lesson[0])
        else:
            return 0
