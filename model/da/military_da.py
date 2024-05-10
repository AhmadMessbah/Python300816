from model.da.da import Da
from model.da.person_da import PersonDa
from model.entity.military import Military


class MilitaryDa(Da):
    def save(self, military):
        if (military.soldier and self.find_soldier_count_by_soldier_id(military.soldier.person_id) < 1):
            self.connect()
            self.cursor.execute(
                "INSERT INTO MILITARY_TBL(serial_number, city, organ, start_date, end_date, soldier_id) VALUES(%s,%s,%s,%s,%s,%s)",
                [military.serial_number,
                 military.city,
                 military.organ,
                 military.start_date,
                 military.end_date,
                 military.soldier.person_id if military.soldier else None])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Soldier Or Cant Save Any More !!!")

    def edit(self, military):
        self.connect()
        self.cursor.execute(
            "UPDATE MILITARY_TBL SET serial_number=%s, city=%s, organ=%s, start_date=%s, end_date=%s, soldier_id=%s WHERE ID=%s",
            [military.serial_number,
             military.city,
             military.organ,
             military.start_date,
             military.end_date,
             military.soldier.person_id if military.soldier else None,
             military.military_id])
        self.connection.commit()
        self.disconnect()

    def remove(self, military_id):
        self.connect()
        self.cursor.execute("DELETE FROM MILITARY_TBL WHERE ID=%s",
                            [military_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM MILITARY_TBL")
        military_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if military_tuple_list:
            military_list = []
            for military_tuple in military_tuple_list:
                military = Military(military_tuple[1], military_tuple[2],
                                    military_tuple[3], military_tuple[4],
                                    military_tuple[5],
                                    person_da.find_by_id(military_tuple[6]))
                military.military_id = military_tuple[0]
                military_list.append(military)
            return military_list
        else:
            raise ValueError("No Record Found !")

    def find_by_military_id(self, military_id):
        self.connect()
        self.cursor.execute("SELECT * FROM MILITARY_TBL WHERE ID=%s", [military_id])
        military_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if military_tuple:
            military = Military(military_tuple[1], military_tuple[2],
                                military_tuple[3], military_tuple[4],
                                military_tuple[5],
                                person_da.find_by_id(military_tuple[6]))
            military.military_id = military_tuple[0]
            return military
        else:
            raise ValueError("No Record Found !")

    def find_by_serial_number(self, serial_number):
        self.connect()
        self.cursor.execute("SELECT * FROM MILITARY_TBL WHERE SERIAL_NUMBER LIKE %s", [serial_number + "%"])
        military_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if military_tuple_list:
            military_list = []
            for military_tuple in military_tuple_list:
                military = Military(military_tuple[1], military_tuple[2],
                                    military_tuple[3], military_tuple[4],
                                    military_tuple[5],
                                    person_da.find_by_id(military_tuple[6]))
                military.military_id = military_tuple[0]
                military_list.append(military)
            return military_list
        else:
            raise ValueError("No Serial Information Found !")

    def find_by_organ(self, organ):
        self.connect()
        self.cursor.execute("SELECT * FROM MILITARY_TBL WHERE ORGAN LIKE %s", [organ + "%"])
        military_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if military_tuple_list:
            military_list = []
            for military_tuple in military_tuple_list:
                military = Military(military_tuple[1], military_tuple[2],
                                    military_tuple[3], military_tuple[4],
                                    military_tuple[5],
                                    person_da.find_by_id(military_tuple[6]))
                military.military_id = military_tuple[0]
                military_list.append(military)
            return military_list
        else:
            raise ValueError("No Organ Information Found !")

    def find_by_city(self, city):
        self.connect()
        self.cursor.execute("SELECT * FROM MILITARY_TBL WHERE CITY LIKE %s", [city + "%"])
        military_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if military_tuple_list:
            military_list = []
            for military_tuple in military_tuple_list:
                military = Military(military_tuple[1], military_tuple[2],
                                    military_tuple[3], military_tuple[4],
                                    military_tuple[5],
                                    person_da.find_by_id(military_tuple[6]))
                military.military_id = military_tuple[0]
                military_list.append(military)
            return military_list
        else:
            raise ValueError("No City Information Found !")

    def find_by_soldier(self, soldier_id):
        self.connect()
        self.cursor.execute("SELECT * FROM MILITARY_TBL WHERE SOLDIER_ID LIKE %s", [soldier_id + "%"])
        military_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if military_tuple_list:
            military_list = []
            for military_tuple in military_tuple_list:
                military = Military(military_tuple[1], military_tuple[2],
                                    military_tuple[3], military_tuple[4],
                                    military_tuple[5],
                                    person_da.find_by_id(military_tuple[6]))
                military.military_id = military_tuple[0]
                military_list.append(military)
            return military_list
        else:
            raise ValueError("No Record Found !")

    def find_soldier_count_by_soldier_id(self, soldier_id):
        self.connect()
        self.cursor.execute("SELECT COUNT(SOLDIER_ID) FROM MILITARY_TBL WHERE SOLDIER_ID=%s", [soldier_id])
        military = self.cursor.fetchone()
        self.disconnect()
        if military:
            return int(military[0])
        else:
            return 0
