from controller.user_controller import UserController


# TEST PASSED
status, message = UserController.save("REZA1", "yuihuh677", 0,1,4)

# TEST PASSED
# status, message = UserController.edit(1, "ali", "ahmadi1234")
#
# TEST PASSED
# status, message =  UserController.remove(9)
#
# TEST
# status, user_list = UserController.find_all()
#
# TEST
# status, user = UserController.find_by_id(1)
#
# TEST
# status, user_list = UserController.find_by_username("fjhsejifh")
