

with open('space.txt', 'r', encoding='utf-8') as file:
    # Создание базы данных с кораблями
    temporary_data = file.readlines()
    data = []
    for information in range(1, len(temporary_data)):
        temporary_data[information] = temporary_data[information][:-1]
        temporary_data[information] = temporary_data[information].split('*')
        data.append(temporary_data[information])
    data[-1][3] = '5 0'
    # Реализация заданной функции для создания новых координат
    for information in data:
        # Названия переменных сходятся с названиями в задании
        n = int(information[0][5])
        m = int(information[0][6])
        new_x, new_y, direction = 0, 0, []
        t = int(len(information[1]))
        # Рассматривание случая нулевых координат и их замена новыми
        if information[2] == '0 0':
            direction = information[3].split()
            x_d = int(direction[0])
            y_d = int(direction[1])
            if n > 5:
                new_x = n + x_d
            else:
                new_x = -1 * (n + x_d) * 4 + t
            if m > 3:
                new_y = m + t + y_d
            else:
                new_y = -1 * (n + y_d) * m
            information[2] = str(new_x) + ' ' + str(new_y)
        # Вывод заданных кораблей
        if information[0][3] == 'V':
            print(f'{information[0]} - ({information[2]})')

with open('space_new.txt', 'w', encoding='utf-8') as file:
    # Запись списка в файл (формат записи не уточнялся)
    for information in data:
        writer = file.write(str(information))
