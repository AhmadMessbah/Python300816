from model.da.da import Da


class SimCardDa(Da):
    def save(self, SimCard):
        self.connect()
        self.cursor.execute("INSERT INTO SIM_CARD_TBL(NUMBER, OPERATOR, PRICE, OWNER) VALUES(%s,%s,%s,%s)",
                            [SimCard.number, SimCard.operator, SimCard.price, SimCard.owner])
        self.connection.commit()
        self.disconnect()

    def edit(self, sim_card):
        self.connect()
        self.cursor.execute("UPDATE SIM_CARD_TBL SET NUMBER=%s, OPERATOR=%s, PRICE=%s, OWNER=%s WHERE ID=%s",
                            [sim_card.number,
                             sim_card.operator,
                             sim_card.price,
                             sim_card.owner,
                             sim_card.sim_card_id]
                            )
        self.connection.commit()
        self.disconnect()

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
        if sim_card_tuple_list:
            sim_card_list = []
            for sim_card_tuple in sim_card_tuple_list:
                sim_card = SimCardDa(sim_card_tuple[1], sim_card_tuple[2])
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
        if sim_card_tuple:
            sim_card = SimCardDa(sim_card_tuple[1], sim_card_tuple[2])
            sim_card.sim_card_id = sim_card_tuple[0]
            return sim_card
        else:
            raise ValueError("No sim_card Found !")

    def find_by_owner(self, owner):
        self.connect()
        self.cursor.execute("SELECT * FROM SIM_CARD_TBL WHERE OWNER=%s", [owner])
        sim_card_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if sim_card_tuple_list:
            sim_card_list = []
            for sim_card_tuple in sim_card_tuple_list:
                sim_card = SimCardDa(sim_card_tuple[1], sim_card_tuple[2])
                sim_card.sim_card_id = sim_card_tuple[0]
                sim_card_list.append(sim_card)
            return sim_card_list
        else:
            raise ValueError("No sim_card Found !")
