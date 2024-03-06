class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        if speed_change < 0:
            self.current_speed = max(0, self.current_speed + speed_change)
        else:
            self.current_speed = min(self.max_speed, self.current_speed + speed_change)

    def drive(self, hours):
        distance_covered = self.current_speed * hours
        self.distance_traveled += distance_covered


car = Car(200)
car.accelerate(60)
print("Current speed:", car.current_speed)

car.drive(1.5)
print("Travelled distance after driving for 1.5 hours:", car.distance_traveled, "km")
