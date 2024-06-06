from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError('Слишком короткая фамилия')
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер телефона')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()


def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standard_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r) #список со словарями


def remove_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standard_write(file_name, res)
    else:
        print('Введен неверный номер строки')


def copy_data(file_name, second_file):
    copy = int(input('Введите номер строки для копирования: '))
    res = read_file(file_name)
    res2 = read_file(second_file)

    if copy <= len(res):
        res2.append(res[copy-1])
        standard_write(second_file, res2)
        print('Контакт скопирован')
    else:
        print('Введен неверный номер строки')


def edit_data(file_name):
    copy = int(input('Введите номер строки для редактирования: '))
    res = read_file(file_name)
    edit = res[copy-1]

    print("Выберите что изменить: \n 1 - Имя \n 2 - Фамилия \n 3 - Номер телефона")
    command = int(input("Введите число: "))

    if command == 1:
        edit['first_name'] = input('Введите новое имя: ')
    elif command == 2:
        edit['second_name'] = input('Введите новую фамилию: ')
    elif command == 3:
        edit['phone_number'] = input('Введите новый номер телефона: ')

    standard_write(file_name, res)


def standard_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)


file_name = 'phone.csv'
second_file = 'second_file.csv'

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл')
                continue
            remove_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл')
                continue
            copy_data(file_name, second_file)
        elif command == 'e':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл')
                continue
            edit_data(file_name)

main()
