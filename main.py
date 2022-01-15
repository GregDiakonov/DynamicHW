import sys
from timeit import default_timer as timer
from container import *

# Глобальные аргументы, в которых помещаются аргументы из командной строки
file_input_mode = 0
input_file_name = ""
output_file_name = ""
element_number = 0

# Проверка аргументов командной строки
def check_argv():
    if len(sys.argv) != 5:
        print("Not enough command line arguments provided! ")
        return 0

    global file_input_mode, input_file_name, output_file_name, element_number

    if sys.argv[3] == "-f":
        file_input_mode = 1
    elif sys.argv[3] == "-r":
        file_input_mode = 0
    else:
        print("Incorrect input identifier! ")
        return 0

    if int(sys.argv[4]) > 10000 or int(sys.argv[4]) < 1:
        print("Incorrect number of elements! ")
        return 0

    element_number = int(sys.argv[4])

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    try:
        input_file = open(input_file_name)
        input_file.close()
        input_file = open(output_file_name)
        input_file.close()
    except:
        print("A file-related problem has occurred! ")
        return 0
    return 1


# Алгоритм работы программы.
# 1. Введённые аргументы командной строки проверяются.
# 2. Инициализируется контейнер
# 3. В зависимости от режима, контейнер наполняется объектами.
#    При системной генерации в неиспользованный вводный файл вписываются
#    случайно сгенерированные данные.
#    Затем эти данные можно будет перезапустить, используя файловый ввод.
# 4. Подсчёт общей для всех альтернатив функций.
# 5. Сортировка и вывод содержимого контейнера в выходной файл.
if __name__ == '__main__':
    start = timer()
    if check_argv() == 0:
        print("Shutting down...")
        sys.exit()
    container = Container(element_number)
    if file_input_mode:
        unreadable_strings = container.file_input(input_file_name)
        container.length -= unreadable_strings
    else:
        random.seed()
        container.random_input()
        input_file_write = open(input_file_name, "w+")
        for i in range(container.length):
            container.storage[i].raw_output(input_file_write)
    container.count_simple_function()
    container.insertion_sort(output_file_name)
    print("Done! Check out the output file\n")
    end = timer()
    print("Execution time: " + round((end - start), 3).__str__() + " seconds\n")
