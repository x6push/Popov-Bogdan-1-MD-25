# Задание 2.1
def password_check():
    pass1 = input("Введите пароль:   ")
    pass2 = input("Повторите пароль:   ")

    if(pass1 == pass2):
        print("Пароль принят")
    else:
        print("Пароль не принят")

# password_check()

# Задание 2.2
def places(place):
    if(place <= 36):
        if(place % 2 == 0):
            return("Купе верхнее место")
        else:
            return("Купе нижнее место")
    else:
        if(place % 2 == 0):
            return("Боковушка верхнее место")
        else:
            return("Боковушка нижнее место")
#place = int(input("Введите номер места:   "))
#result = places(place)
#print(result)

# Задание 2.3

def is_leap_year(year):
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return f'{year} - високосный'
    else:
        return 'Это год не високосный'
#year = int(input("Введите год:   "))
#result = is_leap_year(year)
#print(result)

# Задание 2.4

def colors(color1, color2):
    if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
        return("Фиолетовый")
    elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
        return("Оранжевый")
    elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
        return("Зеленый")
    else:
        return("Ошибка. Введите корректные названия основных цветов: красный, синий или желтый")

#color1 = input("Введите первый основной цвет (красный, синий или желтый): ").lower()
#color2 = input("Введите второй основной цвет (красный, синий или желтый): ").lower()
#result = colors(color1, color2)
#print(result)