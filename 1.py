class Car:
    def __init__(self, r, m):
        self.reg = r
        self.ms = m
        self.s = 0
        self.d = 0

nc = Car("XYZ-456", 180)

print("Registration Number:", nc.reg)
print("Maximum Speed:", nc.ms, "km/h")
print("Current Speed:", nc.s, "km/h")
print("Travelled Distance:", nc.d, "km")