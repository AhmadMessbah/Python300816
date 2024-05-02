from controller.sim_card_controller import SimCardController

sim_card_controller = SimCardController()

status, message = sim_card_controller.save("09107777777", "irancell", 200, "SinMrf")

# status, message = sim_card_controller.edit(2, "09124444444", "MahyaAhm")
#
# status, message = sim_card_controller.remove(1)
#
# status, sim_card_list = sim_card_controller.find_all()
#
# status, sim_card = sim_card_controller.find_by_id(3)
#
# status, sim_card_list = sim_card_controller.find_by_owner("SinaMrf")
#
#
