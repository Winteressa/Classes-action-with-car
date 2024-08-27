#
class Car:
    def __init__(self, brand, mass=1500, fuel=50, km=500, power=200, speed=220):
        self.mass = mass
        self.fuel = fuel
        self.km = km
        self.power = power
        self.speed = speed
        self.brand = brand

    def __add__(self, other):
        return self.mass + other.mass

    def __str__(self):
        return f"[{self.brand}] {self.mass}kg, {self.power} h.p."

    def drive(self):
        print(f"Driving on {self.brand} [speed: {self.speed}, power: {self.power}]")

    def info(self):
        return f"Бренд: {self.brand}\nМасса: {self.mass}\nВид топлива: {self.fuel}\nПробег: {self.km}\nМощность: {self.power}\nСкорость: {self.speed}"

    def lock(self):
        password = input("введите пароль ")
        if password == "123":
            print("car is closed")
        else:
            print("try again")


    def unlock(self):
        num = 0
        while num != "unlock":
            num = input("Откройте машину: ")
        return f"car is opened"

    def start_engine(self):
        import random
        a = 0
        a = random.random()
        if a < 1000000000:
            print("Машина завелась, поехали!")
        else:
            print("Не завелась, попробуй толкнуть!")

    # как сделать функцию с нажитием клавиши?
    # def stop_engine(self):
    #     import keyboard
    #     print("Ожидание нажатия клавиши 'пробел'")
    #     keyboard.read_key(s)
    #     print("Вы остановились!")


bmw_m5 = Car("BMW", mass=1430, fuel=80, km=470, power=635, speed=305)
kia_k5 = Car("KIA", mass=1511, fuel=60, km=800, power=240, speed=240)
haval = Car("HAVAL")
#
# bmw_m5.drive()
# kia_k5.drive()
# haval.drive()
#
# print(bmw_m5 + kia_k5)
#
# print(haval)

print(bmw_m5.info())
print(bmw_m5.start_engine())
print(bmw_m5.lock())
print(bmw_m5.unlock())
