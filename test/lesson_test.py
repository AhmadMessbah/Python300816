from controller.lesson_controller import LessonController

# # TEST PASSED , save
# status, message = LessonController.save("aaa", "vvv", "Oloomi", 2021, 5, 25)

# TEST PASSED , edit
status, message = LessonController.edit(4, "math", "elementary", "Hafez", 2021, 5, 25)

# TEST PASSED , remove
# status, message = LessonController.remove(4)

# TEST PASSED , find_all
# status, lesson_list = l_controller.find_all()

# TEST PASSED , find_by_id
# status, lesson = l_controller.find_by_id(20)

# TEST PASSED , find_by_name
# status, lesson_list = l_controller.find_by_name("python")

# TEST PASSED , find_by_teacher
# status, lesson_list = l_controller.find_by_teacher("oloomi")

# #
