from controller.military_controller import MilitaryController

# # TEST PASSED , save
#  status, message = MilitaryController.save('21111111111', "aa","aa",2020,2,2,2021,2,2 )
# status, message = MilitaryController.save('11111111111',
#                                           'karaj',
#                                           'alib',
#                                           11,
#                                           21,
#                                           2023,
#                                           5,
#                                           7)

# TEST PASSED , edit
#status, message = MilitaryController.edit(1,'00111111111', "aaaa","aa",1200,2,2,1200,2,5 )

# TEST PASSED , remove
# status, message = MilitaryController.remove(2)

# TEST PASSED , find_all
# status, lesson_list = MilitaryController.find_all()

# TEST PASSED , find_by_id
# status, lesson = MilitaryController.find_by_id(8)

# TEST PASSED , find_by_city
# status, lesson_list = MilitaryController.find_by_city("aab")

# TEST PASSED , find_by_organ
# status, lesson_list = MilitaryController.find_by_organ("aab")

# TEST PASSED , find_by_serial
#  status, lesson_list = MilitaryController.find_by_serial_number("0001")


status, message = MilitaryController.save("11111111111", "tehran", 2021, 5, 25, 1)

