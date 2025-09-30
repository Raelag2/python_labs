minutes = int(input('Минуты: '))
a = minutes // 60
b = minutes - a*60
print(f'{a}:{b:02d}')