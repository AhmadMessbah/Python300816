from controller.lesson_controller import LessonController

l_controller = LessonController()

# # TEST PASSED , save
# status, message = l_controller.save("java", "elementary", "Oloomi", 2018, 12, 25)

# TEST PASSED , edit
# status, message = l_controller.edit(1, "math", "elementary", "Hafez", 2018, 12, 25)

# TEST PASSED , remove
# status, message = l_controller.remove(2)

# TEST PASSED , find_all
# status, lesson_list = l_controller.find_all()

# TEST PASSED , find_by_id
# status, lesson = l_controller.find_by_id(20)

# TEST PASSED , find_by_name
# status, lesson_list = l_controller.find_by_name("python")

# TEST PASSED , find_by_teacher
# status, lesson_list = l_controller.find_by_teacher("oloomi")

# #
# if status:
#     # msg.showinfo()
#     print("Info")
#     print(lesson_list)
# else:
#     # msg.showerror()
#     print("Error")
#     print(lesson_list)
