#  Задание № 1

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Задание №2,3


a = ['в',' ', '"',  '05',  '"', ' ',  'часов', ' ',  '"',  '17',  '"', ' ',  'минут',
      ' ', 'температура', ' ', 'воздуха', ' ', 'была', ' ',  '"',  '+05',  '"', ' ',  'градусов']
print(''.join(a))


#Задание№4

first_name, secod_name, third_name, fouth_name = ['инженер-конструктор Игорь',
            'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
person_1 = f'Уважаемый, {first_name}! Добро пожаловать!'
person_2 = f'Где квартальный отчет, {secod_name.replace("МАРИНА", "Марина")}?Налоговая лютует!'
person_3 = f'{third_name}, ушел в IT!'
person_4 = f'{fouth_name}, с новым годом!'

print(person_1)
print(person_2)
print(person_3.capitalize())
print(person_4.title())
