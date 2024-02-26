import csv
def create_password(information):
    ''' Функция создаёт пароль исходя из данных по кораблю
    Описание аргументов:
    information - Список, содержащий строки с информацией о корабле
    '''

    password = information[1][-3:] + information[0][2] + information[0][1] + information[1][:3][::-1]
    password = password.upper()
    return password

with open('space.txt', 'r', encoding='utf-8') as file:
    # Создание базы данных с кораблями
    temporary_data = file.readlines()
    data = []
    for information in range(1, len(temporary_data)):
        temporary_data[information] = temporary_data[information][:-1]
        temporary_data[information] = temporary_data[information].split('*')
        data.append(temporary_data[information])
    data[-1][3] = '5 0'
    # Добавление пароля следующим элементом в список к информации о каждом корабле
    for information in data:
        information.append(create_password(information))
with open('space_uniq_password.csv', 'w', encoding='utf-8') as file:
    # Запись в csv файл
    writer = csv.writer(file, delimiter='*')
    name = ['ShipName', 'planet', 'coord_place', 'direction', 'password']
    writer.writerow(name)
    writer.writerows(data)