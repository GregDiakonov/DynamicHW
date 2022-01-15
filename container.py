from plane import *
from train import *
from ship import *


class Container:
    # Инициализация контейнера: его длины и списка.
    def __init__(self, length):
        self.length = length
        self.storage = []

    # Метод файлового наполнения контейнера.
    def file_input(self, input_file_name):
        answer_list = []
        failed_strings = 0
        input_file = open(input_file_name)
        data = input_file.read()
        input_file.close()
        strings = data.split("\n")
        for string in strings:
            words = string.split(" ")
            if words[0] == "Plane":
                params_list = [words[1], words[2], words[3], words[4]]
                plane = Plane.input(params_list)
                if plane is None:
                    print("Some lines could not be used to create an object!\n")
                    failed_strings += 1
                    continue
                answer_list.append(plane)
            elif words[0] == "Train":
                params_list = [words[1], words[2], words[3]]
                train = Train.input(params_list)
                if train is None:
                    print("Some lines could not be used to create an object!\n")
                    failed_strings += 1
                    continue
                answer_list.append(train)
            elif words[0] == "Ship":
                params_list = [words[1], words[2], words[3], words[4]]
                ship = Ship.input(params_list)
                if ship is None:
                    print("Some lines could not be used to create an object!\n")
                    failed_strings += 1
                    continue
                answer_list.append(ship)
            else:
                print("Some lines could not be used to create an object! (Could be just blank lines)\n")
                failed_strings += 1
        self.storage = answer_list
        return failed_strings

    # Метод системной генерации содержимого контейнера.
    def random_input(self):
        count = 0
        while count < self.length:
            vehicle_type_dice = random.randint(1, 3)
            if vehicle_type_dice == 1:
                new_plane = Plane.input_random()
                self.storage.append(new_plane)
            elif vehicle_type_dice == 2:
                new_train = Train.input_random()
                self.storage.append(new_train)
            else:
                new_ship = Ship.input_random()
                self.storage.append(new_ship)
            count += 1
        return

    # Метод подсчёта общей функции для всех транспортов в контейнере.
    def count_simple_function(self):
        for vehicle in self.storage:
            vehicle.count_ideal_time()
        return

    # Бинарный поиск
    def binary_search(self, item, low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if item == self.storage[mid].ideal_time:
                return mid + 1
            elif item > self.storage[mid].ideal_time:
                low = mid + 1
            else:
                high = mid - 1
        return low

    # Метод сортировки Binary Insertion Sort
    def insertion_sort(self, output_file_name):
        for i in range(self.length):
            j = i - 1
            selected = self.storage[i].ideal_time

            loc = self.binary_search(selected, 0, j)

            while j >= loc:
                temporary = self.storage[j + 1]
                self.storage[j + 1] = self.storage[j]
                self.storage[j] = temporary
                j -= 1
            self.storage[j + 1].ideal_time = selected

        output_file = open(output_file_name, "w+")
        output_counter = 0
        while output_counter<self.length:
            self.storage[output_counter].output(output_file)
            output_file.write("\n")
            output_counter += 1
        return
