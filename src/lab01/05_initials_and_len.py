fio = str(input('ФИО: '))
lenfio = len(fio.replace(' ', ''))
fio = fio.split()
f = fio[0][0]
i = fio[1][0]
o = fio[2][0]
print('Инициалы:', str(f) + str(i) + str(o))
print('Длина (символов):', lenfio + 2)