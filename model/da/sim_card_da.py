from model.da.da import Da
from model.da.user_da import UserDa
from model.entity.sim_card import SimCard


class SimCardDa(Da):
    def save(self, sim_card):
        if (sim_card.owner and self.find_sim_car_count_by_owner_id(sim_card.owner.user_id)< 3):
            self.connect()
            self.cursor.execute("INSERT INTO SIM_CARD_TBL(NUMBER, OPERATOR, PRICE, OWNER_ID) VALUES(%s,%s,%s,%s)",
                                [sim_card.number,
                                 sim_card.operator,
                                 sim_card.price,
                                 sim_card.owner.user_id if sim_card.owner else None])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Owner Or Cant Save Any More !!!")

    def edit(self, sim_card):
        if (sim_card.owner and self.find_sim_car_count_by_owner_id(sim_card.owner.user_id)< 3):
            self.connect()
            self.cursor.execute("UPDATE SIM_CARD_TBL SET NUMBER=%s, OPERATOR=%s, PRICE=%s, OWNER_ID=%s WHERE ID=%s",
                            [sim_card.number,
                             sim_card.operator,
                             sim_card.price,
                             sim_card.owner.user_id,
                             sim_card.owner.user_id if sim_card.owner else None]
                            )
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Owner Or Cant Save Any More !!!")

    def remove(self, sim_card_id):
        self.connect()
        self.cursor.execute("DELETE FROM SIM_CARD_TBL WHERE ID=%s",
                            [sim_card_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM SIM_CARD_TBL")
        sim_card_tuple_list = self.cursor.fetchall()
        self.disconnect()
        print(sim_card_tuple_list)
        user_da = UserDa()
        if sim_card_tuple_list:
            sim_card_list = []
            for sim_card_tuple in sim_card_tuple_list:
                sim_card = SimCard(
                    sim_card_tuple[1],
                    sim_card_tuple[2],
                    sim_card_tuple[3],
                    user_da.find_by_id(sim_card_tuple[4]))
                sim_card.person_id = sim_card_tuple[0]
                sim_card_list.append(sim_card)
            return sim_card_list
        else:
            raise ValueError("No Sim_Card Found !")

    def find_by_id(self, sim_card_id):
        self.connect()
        self.cursor.execute("SELECT * FROM SIM_CARD_TBL WHERE ID=%s", [sim_card_id])
        sim_card_tuple = self.cursor.fetchone()
        self.disconnect()
        user_da = UserDa()
        if sim_card_tuple:
            sim_card = SimCard(sim_card_tuple[1], sim_card_tuple[2],sim_card_tuple[3],user_da.find_by_id(sim_card_tuple[4]))
            sim_card.sim_card_id = sim_card_tuple[0]
            return sim_card
        else:
            raise ValueError("No sim_card Found !")

    def find_by_owner_id(self, owner_id):
        self.connect()
        self.cursor.execute("SELECT * FROM SIM_CARD_TBL WHERE OWNER_ID=%s", [owner_id])
        sim_card_tuple_list = self.cursor.fetchall()
        self.disconnect()
        user_da = UserDa()
        if sim_card_tuple_list:
            sim_card_list = []
            for sim_card_tuple in sim_card_tuple_list:
                sim_card = SimCard(sim_card_tuple[1], sim_card_tuple[2],sim_card_tuple[3],user_da.find_by_id(sim_card_tuple[4]))
                sim_card.sim_card_id = sim_card_tuple[0]
                sim_card_list.append(sim_card)
            return sim_card_list
        else:
            raise ValueError("No sim_card Found !")

    def find_sim_car_count_by_owner_id(self, owner_id):
        self.connect()
        self.cursor.execute("SELECT * FROM SIM_CARD_COUNT WHERE OWNER_ID=%s", [owner_id])
        sim_count = self.cursor.fetchone()
        self.disconnect()
        if sim_count:
            return int(sim_count[1])
        else:
            return 0