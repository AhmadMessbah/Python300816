from controller.product_controller import ProductController
product_controller = ProductController()



# TEST PASSED
# status , message = product_controller.save("iphonx","Apple","jx1616","1000")
# status , message = product_controller.save("a51","samsung","lk9988","1500")


# TEST PASSED
# status , message = product_controller.edit("1","A51","samsung","XD568","2000")

# TEST PASSED
# status, message = product_controller.remove(1)

# TEST PASSED
# status,message = person_list = product_controller.find_all()
status, message = product_controller.find_by_id(40)
