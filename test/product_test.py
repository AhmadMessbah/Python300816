from controller.product_controller import ProductController




# TEST PASSED
# status , message = ProductController.save("iphonx","Apple","jx1616","1000")
# status , message = ProductController.save("a51","samsung","lk9988","1500")


# TEST PASSED
# status , message = ProductController.edit("4","A51","samsung12","XD568","2000")

# TEST PASSED
status, message = ProductController.remove(4)

# TEST PASSED
# status,message = person_list = ProductController.find_all()
# status, message = ProductController.find_by_id(40)
