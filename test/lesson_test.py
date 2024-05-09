from controller.lesson_controller import LessonController
from controller.person_controller import PersonController

# # TEST PASSED
# status, message = PersonController.save("Reza", "Karimi")
# status, message = LessonController.save("Windows", "elementary", 2022, 7, 21, 2)

# TEST PASSED , edit
# status, message = LessonController.edit(1, "math", "elementary", 2021, 6, 5, 2)

# TEST PASSED , remove
# status, message = LessonController.remove(1)

# TEST PASSED , find_all
# status, lesson_list = LessonController.find_all()

# TEST PASSED , find_by_id
# status, lesson = LessonController.find_by_id(2)

# TEST PASSED , find_by_name
# status, lesson_list = LessonController.find_by_name("Windows")

# TEST PASSED , find_by_teacher
# status, lesson_list = LessonController.find_by_teacher("1")

# TEST PASSED , find_teacher_count_by_teacher_id
# status, message = LessonController.find_teacher_count_by_teacher_id("1")


#