
from model.da.da import Da
from model.da.person_da import PersonDa
from model.entity.car import Car


class CarDa(Da):
    def save(self, car):
        if (car.owner and self.find_car_count_by_owner_id(car.owner.person_id)< 3):
            self.connect()
            self.cursor.execute("INSERT INTO CAR_TBL(MODEL, CAR_BRAND, COLOR, OWNER_ID) VALUES(%s,%s,%s,%s)",
                                [car.model,
                                 car.car_brand,
                                 car.color,
                                 car.owner.person_id if car.owner else None])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Owner Or Cant Save Any More !!!")

    def edit(self, car):
        if (car.owner and self.find_car_count_by_owner_id(car.owner.person_id)< 3):
            self.connect()
            self.cursor.execute("UPDATE CAR_TBL SET MODEL=%s, CAR_BRAND=%s, COLOR=%s, OWNER_ID=%s WHERE ID=%s",
                            [car.model,
                             car.car_brand,
                             car.color,
                             car.owner.person_id if car.owner else None,
                             car.car_id]
                            )
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Owner Or Cant Save Any More !!!")

    def remove(self, car_id):
        self.connect()
        self.cursor.execute("DELETE FROM CAR_TBL WHERE ID=%s",
                            [car_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_TBL")
        car_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if car_tuple_list:
            car_list = []
            for car_tuple in car_tuple_list:
                car = Car(
                    car_tuple[1],
                    car_tuple[2],
                    car_tuple[3],
                    person_da.find_by_id(car_tuple[4]))
                car.car_id = car_tuple[0]
                car_list.append(car)
            return car_list
        else:
            raise ValueError("No Car Found !")

    def find_by_id(self, car_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_TBL WHERE ID=%s", [car_id])
        car_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if car_tuple:
            car = Car(car_tuple[1], car_tuple[2],car_tuple[3],person_da.find_by_id(car_tuple[4]))
            car.car_id = car_tuple[0]
            return car
        else:
            raise ValueError("No car Found !")

    def find_by_owner_id(self, owner_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_TBL WHERE OWNER_ID=%s", [owner_id])
        car_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if car_tuple_list:
            car_list = []
            for car_tuple in car_tuple_list:
                car = Car(car_tuple[1], car_tuple[2],car_tuple[3],person_da.find_by_id(car_tuple[4]))
                car.car_id = car_tuple[0]
                car_list.append(car)
            return car_list
        else:
            raise ValueError("No car Found !")

    def find_car_count_by_owner_id(self, owner_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_COUNT WHERE OWNER_ID=%s", [owner_id])
        CAR_count = self.cursor.fetchone()
        self.disconnect()
        if CAR_count:
            return int(CAR_count[1])
        else:
            return 0





