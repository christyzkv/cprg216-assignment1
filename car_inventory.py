DATA_FILE = "data.txt"


class Car:
    def __init__(self, car_id, name, make, body, year, value):
        self.id = car_id
        self.name = name
        self.make = make
        self.body = body
        self.year = year
        self.value = value

    def __str__(self):
        return "{:<8} {:<18} {:<8} {:<8} {:<8} {}".format(
            self.id,
            self.name,
            self.make,
            self.body,
            self.year,
            float(self.value)
        )


def load_data():
    cars = []
    try:
        file = open(DATA_FILE, "r")
        lines = file.readlines()
        file.close()

        i = 0
        while i < len(lines):
            car_id = int(lines[i])
            name = lines[i + 1].replace("\n", "")
            make = lines[i + 2].replace("\n", "")
            body = lines[i + 3].replace("\n", "")
            year = int(lines[i + 4])
            value = float(lines[i + 5])

            cars.append(Car(car_id, name, make, body, year, value))
            i = i + 6
    except FileNotFoundError:
        pass

    return cars


def save_data(cars):
    file = open(DATA_FILE, "w")
    for car in cars:
        file.write(str(car.id) + "\n")
        file.write(car.name + "\n")
        file.write(car.make + "\n")
        file.write(car.body + "\n")
        file.write(str(car.year) + "\n")
        file.write(str(car.value) + "\n")
    file.close()
    print("Data saved to local file successfully!")

def find_by_id(cars, car_id):
    for car in cars:
        if car.id == car_id:
            return car
    return None


def find_by_name(cars, name):
    for car in cars:
        if car.name == name:
            return car
    return None


def add_car(cars):
    while True:
        print("Enter id of the car, followed by the car's information.")

        car_id = int(input("Id:\n"))
        name = input("name:\n")
        make = input("make:\n")
        body = input("Body:\n")
        year = int(input("year:\n"))
        value = float(input("value:\n"))

        if find_by_id(cars, car_id):
            print("Incorrect Id. Id already exist in the system.")
        else:
            duplicate = False
            for car in cars:
                if car.name == name and car.make == make and car.body == body and car.year == year:
                    print("The car is already in the inventory. No action is required..")
                    duplicate = True
                    break

            if not duplicate:
                cars.append(Car(car_id, name, make, body, year, value))
                print("car is added to the inventory.")
                print(cars[-1])

        again = input("Do you want to add more cars? y(yes)/n(no)\n")
        if again.lower() != "y":
            break


def search_car(cars):
    while True:
        print("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
        choice = int(input())

        if choice == -1:
            break

        if choice == 1:
            car_id = int(input("Please Enter the id of the car:\n"))
            car = find_by_id(cars, car_id)
            if car:
                print("Car found ", car)
            else:
                print("Car not found")

        if choice == 2:
            name = input("Please Enter the name of the car:\n")
            car = find_by_name(cars, name)
            if car:
                print("Car found ", car)
            else:
                print("Car not found")


def edit_car(cars):
    while True:
        car_id = int(input("Enter the id of the car. Enter -1 to return to the previous menu\n"))
        if car_id == -1:
            break

        car = find_by_id(cars, car_id)
        if car:
            car.name = input("Name:\n")
            car.make = input("make:\n")
            car.body = input("Body:\n")
            car.year = int(input("year:\n"))
            car.value = float(input("value:\n"))
            print("Car's new info is", car)
        else:
            print("Car not found")


def remove_car(cars):
    while True:
        print("Enter id of the car that you want to remove from the inventory.")
        car_id = int(input("id:\n"))

        car = find_by_id(cars, car_id)
        if car:
            cars.remove(car)
            print("car removed")
        else:
            print("Car not found")

        again = input("Do you want to remove more cars? y(yes)/n(no) ")
        if again.lower() != "y":
            break


def print_cars(cars):
    for car in cars:
        print(car)


def main():
    cars = load_data()
    print("Welcome to the cars inventory system")

    while True:
        print("What would you like to do today?")
        print("-Add a car? enter 1")
        print("-Search for car? enter 2")
        print("-Edit car info? enter 3")
        print("-Remove a car? enter 4")
        print("-Print the car list? enter 5")
        print("-Save the data to a file? enter 6")
        print("-Exit? enter 0.")

        choice = int(input())

        if choice == 1:
            add_car(cars)
        elif choice == 2:
            search_car(cars)
        elif choice == 3:
            edit_car(cars)
        elif choice == 4:
            remove_car(cars)
        elif choice == 5:
            print_cars(cars)
        elif choice == 6:
            save_data(cars)
        elif choice == 0:
            break


main()
