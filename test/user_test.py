from controller.user_controller import UserController

# TEST
status, message = UserController.save("REZA", "yuihuh8uhi", 0,1)

# TEST PASSED
# status, message = UserController.edit(1, "alireza", "alipour23")
#
# TEST PASSED
# status, message =  UserController.remove(2)
#
# TEST PASSED
# status, user_list = UserController.find_all()
#
# TEST
status, user = UserController.find_by_id(1)
#
# TEST
# status, user_list = UserController.find_by_username("edfs")
