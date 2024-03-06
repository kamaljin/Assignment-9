class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, change):
        if change < 0:
            self.speed = max(0, self.speed + change)
        else:
            self.speed = min(self.max_speed, self.speed + change)


car = Car(200)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Current speed:", car.speed)

car.accelerate(-200)
print("Final speed:", car.speed)
