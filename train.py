import random
from vehicle import *


class Train(Vehicle):
    def __init__(self):
        super(Train, self).__init__()
        self.wagon_number = 0

    @staticmethod
    def input(params_list):
        train = Train()
        try:
            train.speed = int(params_list[0])
            train.way_length = float(params_list[1])
            train.wagon_number = int(params_list[2])
        except ValueError:
            return None
        return train

    @staticmethod
    def input_random():
        train = Train()
        train.speed = random.randint(20, 70)
        train.way_length = (random.randint(100, 9999) + random.random())
        train.way_length = round(train.way_length, 3)
        train.wagon_number = random.randint(5, 20)
        return train

    def output(self, output_file):
        output_file.write("Train\n")
        super().output(output_file)
        output_file.write("Wagon Number: " + self.wagon_number.__str__() + "\n")

    def raw_output(self, output_file):
        output_file.write("Train ")
        super().raw_output(output_file)
        output_file.write(self.wagon_number.__str__() + "\n")
