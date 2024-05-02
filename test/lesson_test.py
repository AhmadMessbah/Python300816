from controller.lesson_controller import LessonController

# # TEST PASSED , save
status, message = LessonController.save("java", "elementary", "Oloomi", 2018, 12, 25)

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
if status:
    # msg.showinfo()
    print("Info")
    print(message)
else:
    # msg.showerror()
    print("Error")
    print(message)
