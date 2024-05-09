from controller.lesson_controller import LessonController
from controller.person_controller import PersonController

# # TEST PASSED , save #TODO
# status, message = PersonController.save("Arash", "Oloomi")
status, message = LessonController.save("Windows", "elementary", 2021, 5, 25, 1)

# TEST PASSED , edit
# status, message = LessonController.edit(6, "math", "elementary", "Hafez", 2021, 5, 10)

# TEST PASSED , remove
# status, message = LessonController.remove(8)

# TEST PASSED , find_all
# status, lesson_list = LessonController.find_all()

# TEST PASSED , find_by_id
# status, lesson = LessonController.find_by_id(6)

# TEST PASSED , find_by_name
# status, lesson_list = LessonController.find_by_name("python")

# TEST PASSED , find_by_teacher
# status, lesson_list = LessonController.find_by_teacher("oloomi")

# #
