def show_menu() -> int:
    print("Телефонный справочник:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу\n"
    "Введите номер необходимого действия: ")
    choice = int(input())
    return choice

def display_the_phone_book(filename: str, fields: list):
    data = read_csv(filename)
    view_list_contact(fields, data)

def find_contact(filename: str, fields: list, number: int):
    data = read_csv(filename)
    message = f'Введите "{fields[number]}" для поиска: '
    name = user_input_string(message)
    contact = list(filter(lambda item: item[number] == name, data))
    view_list_contact(fields, contact)

def add_contact(filename: str, fields: list):
    data = []
    for item in range(4):
        message = f'Введите "{fields[item]}" для записи: '
        data.append(user_input_string(message))
    write_csv(filename, data)

def save_phone_book_in_txt_file(filename_read: str, filename_write: str, fields: list):
    write_to_file(filename_write, fields, read_csv(filename_read))

def user_input_number(message: str, begin: int, end: int) -> int:
    number = int()
    while not (begin <= number <= end):
        string = input(f'{message}')
        number = int(string) if string.isdigit() else int()
    return number

def user_input_string(message: str) -> str:
    string = str()
    while not string:
        string = input(f'{message}')
    return string

def read_csv(filename: str) -> list:
    data = []
    with open(filename, 'r', encoding='utf-8') as phonebook:
        for line in phonebook:
            temp = line.strip().split(',')
            if len(temp) == 4:
                data.append(temp)
    phonebook.close()
    return data

def write_csv(filename: str, data: list):
    with open(filename, 'a') as data_write:
        data_write.write('\n'+','.join(data))

def write_to_file(file_name: str, fields: list, contacts: list):
    data = f'{"-"*73}\n{list_to_string(fields)}\n{"-"*72}\n'
    for item in contacts:
        data += f'{list_to_string(item)}\n'
    data += f'{"-"*73}\n'
    with open(file_name, 'w') as data_write:
        data_write.write(data)

def view_list_contact(fields: list, contacts: list):
    print(f'{"-"*73}')
    print(f'{list_to_string(fields)}')
    print(f'{"-"*73}')
    for item in contacts:
        print(f'{list_to_string(item)}')
    print(f'{"-"*73}')

def list_to_string(data: list) -> str:
    if data[0] == data[1] == data[2] == data[3]
    return f'| {data[0]:<20} | {data[1]:<20} | {data[2]:<10} | {data[3]:<10} |'

def main():
    # csv_file = 'phonebook.csv'
    # txt_file = 'phonebook.txt'
    # fields = ['Фамилия', 'Имя', 'Телефон', "Описание"]
    choice = int()
    while choice != 6:
        choice = show_menu()
        if choice == 1:
            display_the_phone_book(csv_file, fields)
        elif choice == 2:
            find_contact(csv_file, fields, 0)
        elif choice == 3:
            find_contact(csv_file, fields, 2)
        elif choice == 4:
            add_contact(csv_file, fields)
        elif choice == 5:
            save_phone_book_in_txt_file(csv_file, txt_file, fields)

csv_file = 'phonebook.csv'
txt_file = 'phonebook.txt'
fields = ['Фамилия', 'Имя', 'Телефон', "Описание"]
#choice = int()
main()