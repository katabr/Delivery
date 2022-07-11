
# Реализация функции с вводом данных с клавиатуры


# Вводим значение для хрупкости
def fragility():
    a = "Хрупкость"
    global f
    global frag
    cost_f = 0
    while ((a != "Y") and (a != "N")):
        print("Хрупкий ли Ваш товар (Y/N)?")
        a = input()
        if a == "Y":
            frag = True
            f = "Хрупкий"
            cost_f = 200
            print(f)
        elif a == "N":
            frag = False
            f = "Не хрупкий"
            print(f)
        else:
            print("Данные введены некорректно. Введите Y/N.")
    print(f"Надбавка за хрупкость составит {cost_f} рублей.")
    return cost_f


# Вводим расстояние доставки
def distance():
    print("Введите расстояние для доставки в км.")
    global s
    cost_s = 0
    s = float(input())


    while ((s > 30) and (frag ==True)):
        #if ((fragility = True) and (s > 30)):
        print ("Хрупкие товары не могут быть доставлены далее 30 км. Введите другое расстояние.")
        s = float(input())
    while ((s < 0)):
        # if ((fragility = True) and (s > 30)):
        print("Расстояние не может быть отрицательным. Введите другое расстояние.")
        s = float(input())

    if s > 30:
        cost_s = 300
    elif 30 >= s > 10:
        cost_s = 200
    elif 10 >= s > 2:
        cost_s = 100
    elif 2 >= s >= 0:
        cost_s = 50
    print(f"Надбавка за расстояние составит {cost_s} рублей.")
    return cost_s

# Вводим размеры (возвращает добавку по габаритам)
def dimensions():
    d = "Размеры"
    global ds
    while ((d != "big") and (d != "small")):
        print("Введите габариты товара (big/small)?")
        d = input()
        if d == "big":
            cost_d = 200
            ds = "Большие"
            print(ds)
        elif d == "small":
            cost_d = 100
            ds = "Не большие"
            print(ds)
        else:
            print("Данные введены некорректно. Введите big/small.")
    print(f"Надбавка за габариты составит {cost_d} рублей.")
    return cost_d

# Вводим загруженность (возвращает множитель)
def workload():
    print("Введите повышенную загруженность, если есть\n-vh - Очень высокая\n-h - Высокая\n-aa - Выше среднего")
    l = input()
    global wl
    if l == "vh":
        wld = 1.6
        wl = "Очень высокая"
    elif l == "h":
        wld = 1.4
        wl = "Высокая"
    elif l == "h":
        wld = 1.2
        wl = "Выше среднего"
    else:
        wld = 1
        wl = "Обычная"
    print(wl)
    print(f"Множитель за загруженность составит {wld}.")
    return wld

def cost_of_delivery():
    delivery = 0
    delivery = (delivery + fragility() + distance() + dimensions())*int(workload())
    return delivery

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    delivery = cost_of_delivery()

    print(f"Ваши параметры:\nХрупкость - {f}\nРасстояние - {s} км\nГабариты - {ds}\nЗагруженность - {wl}")
    print(f"Расчетная стоимость доставки составит {delivery} рублей.")
    if delivery < 400:
        delivery = 400
        print(f"Расчетная соимость доставки меньше минимальной.\nМинимальная стоимость доставки составит - {delivery} рублей.")



