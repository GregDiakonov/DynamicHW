class Vehicle:
    # Определение общих полей для всех транспортных средств.
    def __init__(self):
        self.speed = 0
        self.way_length = 0.0
        self.ideal_time = 0.0

    # В классах-наследниках этот метод отвечает за создание новых транспортных средств.
    # Основа: информация из файлов
    @staticmethod
    def input(params_list):
        pass

    # В классах-наследниках этот метод отвечает за создание новых транспортных средств.
    # Основа: системно сгенерированная информация
    @staticmethod
    def input_random():
        pass

    # Метод, выводящий информацию в выходной файл.
    def output(self, output):
        output.write("Speed: " + self.speed.__str__() + "\n")
        output.write("Way Length: " + self.way_length.__str__() + "\n")
        output.write("Ideal time of arrival: " + self.ideal_time.__str__() + "\n")
        return

    # Метод, выводящий информацию в такой форме, чтобы программа смогла прочитать эти данные из файла позднее.
    def raw_output(self, output_file):
        output_file.write(self.speed.__str__() + " " +
                          self.way_length.__str__() + " ")
        return

    # Общая для всех альтернатив функция.
    def count_ideal_time(self):
        self.ideal_time = self.way_length/self.speed
        self.ideal_time = round(self.ideal_time, 3)
