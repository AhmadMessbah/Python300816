from controller.user_controller import UserController


# TEST PASSED
# UserController.save("REZA", "yuihuh677", 0,1,1)

# TEST PASSED
# UserController.edit(1, "ali", "ahmadi1234",1,0,2)
#
# TEST
# status, message =  UserController.remove(9)
#
# TEST
# status, user_list = UserController.find_all()
#
# TEST
# UserController.find_by_id(1)
#
# TEST
print(UserController.find_by_username("ali"))
