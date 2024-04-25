from controller.lesson_controller import LessonController

l_controller = LessonController()

# TEST PASSED , save
# status, message = l_controller.save("math", "elementary", "Mesbah", 2018, 12, 25)

# TEST PASSED , edit
status, message = l_controller.edit(1, "math", "elementary", "Hafez", 2018, 12, 25)

# TEST PASSED , remove
# status, message =  l_controller.remove(1)

# TEST PASSED , find_all
# status, lesson_list = l_controller.find_all()

# TEST PASSED , find_by_id
# status, lesson = l_controller.find_by_id(4)

# TEST PASSED , find_by_name
# status, lesson_list = l_controller.find_by_name("math")

# TEST PASSED , find_by_teacher
# status, lesson_list = l_controller.find_by_name("Hafez")


if status:
    # msg.showinfo()
    print("Info")
    print(message)
else:
    # msg.showerror()
    print("Error")
    print(message)
