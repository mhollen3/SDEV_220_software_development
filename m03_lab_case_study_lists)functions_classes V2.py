
def user_year(self):
    self.year = input(
        "Please enter the year your vehicle was produced:    ")
    return self.year


def user_make(self):
    self.make = input("Please enter the make of your vehicle:    ")
    return self.make


def user_model(self):
    self.model = input("Please enter the model of your vehicle:    ")
    return self.model


def user_doors(self):
    self.doors = input(
        "Please enter the number of doors your vehicle has:    ")
    return self.doors


def user_roof(self):
    self.roof = input(
        "Please enter the style of roof your vehicle has:    ")
    return self.roof


class Vehicle():
    def __init__(self, type):
        self.type = type


def user_type(self):
    self.type = input("Please enter the type of vehicle you own:    ")
    return self.type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def description(self):
        print("Vehicle type:", self.type,
              "Vehicle year:", self.year,
              "Vehicle make:", self.make,
              "Vehicle model:", self.model,
              "Vehicle doors:", self.doors,
              "Vehicle roof:", self.roof,
              )
        return self.description


car1 = Automobile(user_year, user_make, user_model, user_doors, user_roof)

print(car1.description())
