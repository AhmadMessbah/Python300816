from model.da.da import Da
from model.da.user_da import UserDa
from model.entity.car import Car


class CarDa(Da):
    def save(self, car):
        if (car.owner and self.find_car_count_by_owner_id(car.owner.user_id)< 3):
            self.connect()
            self.cursor.execute("INSERT INTO CAR_TBL(MODEL, NAME, COLOR, OWNER_ID) VALUES(%s,%s,%s,%s)",
                                [car.model,
                                 car.name,
                                 car.color,
                                 car.owner.user_id if car.owner else None])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Owner Or Cant Save Any More !!!")

    def edit(self, car):
        if (car.owner and self.find_car_count_by_owner_id(car.owner.user_id)< 3):
            self.connect()
            self.cursor.execute("UPDATE CAR_TBL SET MODEL=%s, NAME=%s, COLOR=%s, OWNER_ID=%s WHERE ID=%s",
                            [car.model,
                             car.name,
                             car.color,
                             car.owner.user_id,
                             car.owner.user_id if car.owner else None]
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
        print(car_tuple_list)
        user_da = UserDa()
        if car_tuple_list:
            car_list = []
            for car_tuple in car_tuple_list:
                car = Car(
                    car_tuple[1],
                    car_tuple[2],
                    car_tuple[3],
                    user_da.find_by_id(car_tuple[4]))
                car.person_id = car_tuple[0]
                car_list.append(car)
            return car_list
        else:
            raise ValueError("No Car Found !")

    def find_by_id(self, car_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_TBL WHERE ID=%s", [car_id])
        car_tuple = self.cursor.fetchone()
        self.disconnect()
        user_da = UserDa()
        if car_tuple:
            car = Car(car_tuple[1], car_tuple[2],car_tuple[3],user_da.find_by_id(car_tuple[4]))
            car.car_id = car_tuple[0]
            return car
        else:
            raise ValueError("No car Found !")

    def find_by_owner_id(self, owner_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_TBL WHERE OWNER_ID=%s", [owner_id])
        car_tuple_list = self.cursor.fetchall()
        self.disconnect()
        user_da = UserDa()
        if car_tuple_list:
            car_list = []
            for car_tuple in car_tuple_list:
                car = CaR(car_tuple[1], car_tuple[2],car_tuple[3],user_da.find_by_id(car_tuple[4]))
                car.car_id = car_tuple[0]
                car_list.append(car)
            return car_list
        else:
            raise ValueError("No car Found !")

    def find_car_count_by_owner_id(self, owner_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CAR_COUNT WHERE OWNER_ID=%s", [owner_id])
        carr_count = self.cursor.fetchone()
        self.disconnect()
        if carr_count:
            return int(carr_count[1])
        else:
            return 0