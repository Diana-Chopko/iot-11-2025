from enum import Enum
import time


class Brand(Enum):
    TOYOTA = "Toyota"
    AUDI = "Audi"
    MAZDA= "Mazda"
    BMW = "BMW"
    TESLA = "Tesla"


class Car:
    def __init__(self, brand: Brand, age, max_speed, horse_power):
        self.brand = brand
        if age <= 0:
            raise ValueError("Вік авто має бути більшим 0")
        self.age = age
        if max_speed <= 0:
            raise ValueError("Максимальна швидкість авто має бути більшою 0")
        self.max_speed = max_speed
        if horse_power <= 0:
            raise ValueError("Кількість кінських сил має бути більшою 0")
        self.horse_power = horse_power
        self.start_time = 0
        self.end_time = 0

    def time_park(self):
        self.start_time = time.time()

    def time_leave(self):
        self.end_time = time.time()

    def parking_duration_hours(self):
        parking_time = 0
        if self.start_time:
            if self.end_time:
                end = self.end_time
            else:
                end = time.time()
            parking_time = (end - self.start_time) / 3600
        return parking_time


class Parking:
    price_per_hour = 50

    def __init__(self, max_places):
        self.max_places = max_places
        self.cars_on_parking = []
        self.history = []

    def park_car(self, car: Car):
        if len(self.cars_on_parking) >= self.max_places:
            print("🔴 Паркінг переповнений 🔴")
        else:
            car.time_park()
            self.cars_on_parking.append(car)
            print(f"Авто {car.brand.value} припарковано")

    def leave_parking(self, car: Car):
        if car in self.cars_on_parking:
            car.time_leave()
            self.cars_on_parking.remove(car)
            self.history.append(car)
            print(f"Авто {car.brand.value} виїхало зі стоянки")
        else:
            print("Цього авто немає на парковці")

    def sorting_cars_by_duration(self):
        # беремо і тих, що ще стоять, і тих, що вже виїхали
        all_cars = self.cars_on_parking + self.history
        return sorted(all_cars, key=lambda x: x.parking_duration_hours(), reverse=True)

    def calculate_parking_price(self, car: Car):
        hours = car.parking_duration_hours()
        return round(hours * self.price_per_hour, 2)


def main():
    parking = Parking(3)

    car_1 = Car(Brand.MAZDA, 1, 240, 110)
    car_2 = Car(Brand.AUDI, 3, 280, 140)
    car_3 = Car(Brand.TOYOTA, 12, 240, 135)
    car_4 = Car(Brand.TESLA, 2, 260, 120)

    parking.park_car(car_1)
    parking.park_car(car_2)
    parking.park_car(car_3)
    parking.park_car(car_4)

    time.sleep(2.5)
    parking.leave_parking(car_1)

    time.sleep(2)
    parking.leave_parking(car_2)

    sorted_cars = parking.sorting_cars_by_duration()
    print("\nСортування за тривалістю стоянки:")
    for car in sorted_cars:
        print(f"{car.brand.value}: {car.parking_duration_hours():.4f} год")

    print("\nЦіна стоянки:")
    for car in sorted_cars:
        print(f"{car.brand.value}: {parking.calculate_parking_price(car)} грн")


if __name__ == "__main__":
    main()
