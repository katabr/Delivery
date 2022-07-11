

# Реализация функции с вводом данных через параметры

# frag = True, False, другое
# s = число 0,2, 10,30
# d = big, small, другое
# l = vh, h, aa, другое

frag = False
s = 350
d = "big"
l = "vh"

class Delivery():
    def fragility(self, frag):
        # a = "Хрупкость"
        global f
        #global frag
        cost_f = 0
        #while ((a != "Y") and (a != "N")):
        #   print("Хрупкий ли Ваш товар (Y/N)?")
        #   a = input()
        if frag == True:
            f = "Хрупкий"
            cost_f = 200

        elif frag == False:
            #frag = False
            f = "Не хрупкий"

        else:
            print("Данные введены некорректно. Введите True or False.")
        print(f"Надбавка за хрупкость составит {cost_f} рублей.")
        return cost_f


    # Вводим расстояние доставки
    def distance(self, frag, s):
        #print("Введите расстояние для доставки в км.")
        global st
        st = s
        cost_s = 0
        #s = float(input())


        while ((s > 30) and (frag ==True)):
            #if ((fragility = True) and (s > 30)):
            print ("Хрупкие товары не могут быть доставлены далее 30 км. Введите другое расстояние.")
            #s = float(input())
        while ((s < 0)):
            # if ((fragility = True) and (s > 30)):
            print("Расстояние не может быть отрицательным. Введите другое расстояние.")
            #s = float(input())

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
    def dimensions(self, d):
        #d = "Размеры"
        global ds
        #while ((d != "big") and (d != "small")):
            #print("Введите габариты товара (big/small)?")
            #d = input()
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
    def workload(self, l):
        #print("Введите повышенную загруженность, если есть\n-vh - Очень высокая\n-h - Высокая\n-aa - Выше среднего")
        #l = input()
        global wl
        if l == "vh":
            wld = 1.6
            wl = "Очень высокая"
        elif l == "h":
            wld = 1.4
            wl = "Высокая"
        elif l == "aa":
            wld = 1.2
            wl = "Выше среднего"
        else:
            wld = 1
            wl = "Обычная"
        print(wl)
        print(f"Множитель за загруженность составит {wld}.")
        return wld

    def cost_of_delivery(self, frag, s, d, l):
        delivery = 0
        delivery = (delivery + self.fragility(frag) + self.distance(s) + self.dimensions(d))*self.workload(l)
        return delivery

    def full_cost_of_delivery(self, frag, s, d, l):
        delivery = 0
        delivery = (delivery + self.fragility(frag) + self.distance(s) + self.dimensions(d))*self.workload(l)
        if delivery < 400:
            delivery = 400
        return delivery

if __name__ == '__main__':

    devl = Delivery
    delivery = devl.cost_of_delivery( frag, s, d, l)
    fill_delivery = devl.full_cost_of_delivery(frag, s, d, l)
    print(f"Ваши параметры:\nХрупкость - {f}\nРасстояние - {st} км\nГабариты - {ds}\nЗагруженность - {wl}")
    print(f"Расчетная стоимость доставки составит {delivery} рублей.")
    if delivery < 400:
        delivery = 400
        print(f"Расчетная соимость доставки меньше минимальной.\nМинимальная стоимость доставки составит - {delivery} рублей.")
