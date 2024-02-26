with open('space.txt', 'r', encoding='utf-8') as file:
    # Создание базы данных с кораблями
    temporary_data = file.readlines()
    data = []
    for information in range(1, len(temporary_data)):
        temporary_data[information] = temporary_data[information][:-1]
        temporary_data[information] = temporary_data[information].split('*')
        data.append(temporary_data[information])
    data[-1][3] = '5 0'
    # Алгоритм по поиску корабля в базе данных
    ShipName = input()
    # Цикл с условием окончания
    while ShipName != 'stop':
        for information in data:
            # Нахождение названия корабля в базе данных
            if information[0] == ShipName:
                print(f'Корабль {information[0]} был отправлен с планеты: {information[1]} и его направление движения было: {information[3]}')
                # Конец поиска если в базе данных 1 корабль с таким названием
                break
        else:
            # Вывод ошибки при условии ненахождения корабля
            print('error.. er.. ror..')
        # Продолжение работы алгоритма
        ShipName = input()

