a = input('Введите температуру в градусах цельсия или в фаренгейта\n')
try:
    a = a[0:-1]
    a=int(a)
except ValueError:
    print('Данные введены неверно')
else:
    if a[-1] == 'F' or a[-1] == 'f':
        a = str((a-32)*5/9)
        print (a + 'C')
    elif a[-1] == 'C' or a[-1] == 'c':
        a = str((a*9/5)+32)
        print (a + 'F')
    else:
        print ('Некорректный ввод данных')
