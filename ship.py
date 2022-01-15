import random
from vehicle import *
from enum import Enum


class ShipType(Enum):
    LINER = 1
    TUGBOAT = 2
    TANKER = 3


class Ship(Vehicle):
    def __init__(self):
        super(Ship, self).__init__()
        self.tonnage = 0
        self.ship_type = ShipType.LINER

    @staticmethod
    def input(params_list):
        ship = Ship()
        try:
            ship.speed = int(params_list[0])
            ship.way_length = float(params_list[1])
            ship.tonnage = int(params_list[2])
        except ValueError:
            return None
        if params_list[3] == "Liner":
            ship.ship_type = ShipType.LINER
        elif params_list[3] == "Tugboat":
            ship.ship_type = ShipType.TUGBOAT
        elif params_list[3] == "Tanker":
            ship.ship_type = ShipType.TANKER
        else:
            return None
        return ship

    @staticmethod
    def input_random():
        ship = Ship()
        ship.speed = random.randint(50, 70)
        ship.way_length = (random.randint(100, 9999) + random.random())
        ship.way_length = round(ship.way_length, 3)
        ship.tonnage = random.randint(1000, 2000)
        ship_type_dice = random.randint(1, 3)
        if ship_type_dice == 1:
            ship.ship_type = ShipType.LINER
        elif ship_type_dice == 2:
            ship.ship_type = ShipType.TUGBOAT
        else:
            ship.ship_type = ShipType.TANKER
        return ship

    def output(self, output_file):
        output_file.write("Ship\n")
        super().output(output_file)
        output_file.write("Tonnage: " + self.tonnage.__str__() + "\n")
        if self.ship_type == ShipType.LINER:
            output_file.write("Type: Liner\n")
        elif self.ship_type == ShipType.TUGBOAT:
            output_file.write("Type: Tugboat\n")
        else:
            output_file.write("Type: Tanker\n")
        return

    def raw_output(self, output_file):
        output_file.write("Ship ")
        super().raw_output(output_file)
        output_file.write(self.tonnage.__str__() + " ")
        if self.ship_type == ShipType.LINER:
            output_file.write("Liner\n")
        elif self.ship_type == ShipType.TUGBOAT:
            output_file.write("Tugboat\n")
        else:
            output_file.write("Tanker\n")
