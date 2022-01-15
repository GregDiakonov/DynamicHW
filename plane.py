import random
from vehicle import *


class Plane(Vehicle):
    def __init__(self):
        super(Plane, self).__init__()
        self.capacity = 0
        self.flight_radius = 0

    @staticmethod
    def input(params_list):
        plane = Plane()
        try:
            plane.speed = int(params_list[0])
            plane.way_length = float(params_list[1])
            plane.capacity = int(params_list[2])
            plane.flight_radius = int(params_list[3])
        except ValueError:
            return None
        return plane

    @staticmethod
    def input_random():
        plane = Plane()
        plane.speed = random.randint(200, 1000)
        plane.way_length = (random.randint(0, 9999) + random.random())
        plane.way_length = round(plane.way_length, 3)
        plane.capacity = random.randint(10, 100)
        plane.flight_radius = random.randint(1, 10000)
        return plane

    def output(self, output_file):
        output_file.write("Plane\n")
        super().output(output_file)
        output_file.write("Capacity: " + self.capacity.__str__() + "\n")
        output_file.write("Flight radius: " + self.flight_radius.__str__() + "\n")

    def raw_output(self, output_file):
        output_file.write("Plane ")
        super().raw_output(output_file)
        output_file.write(self.capacity.__str__() + " " +
                          self. flight_radius.__str__() + "\n")
