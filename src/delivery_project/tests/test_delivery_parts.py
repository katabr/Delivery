import unittest

from ..functions.delivery import Delivery



class TestDeliveryParts(unittest.TestCase, Delivery):
    delv = Delivery

    # Проверка классов эквивалентности для параметра Хрупкость
    def test_fragility_true(self):
        delv = Delivery
        frag = True
        cost = delv.fragility(frag)
        assert cost == 200

    def test_fragility_false(self):
        delv = Delivery
        frag = "Fail"
        delv.fragility(frag)
        assert "Данные введены некорректно. Введите True or False."

    def test_fragility_fail(self):
        delv = Delivery
        frag = False
        delv.fragility(frag)
        assert cost == 0

    # Проверка классов эквивалентности для параметра Дальность
    def test_distance_minus(self):
        delv = Delivery
        frag = False
        s  = -3
        delv.fragility(frag, s)
        assert  "Расстояние не может быть отрицательным. Введите другое расстояние."


    def test_distance_0(self):
        delv = Delivery
        frag = False
        s = 0
        cost = delv.fragility(frag, s)
        assert cost == 0

    def test_distance_0_5(self):
        delv = Delivery
        frag = False
        s = 0.5
        cost = delv.fragility(frag, s)
        assert cost == 50

    def test_distance_2(self):
        delv = Delivery
        frag = False
        s = 2
        cost = delv.fragility(frag, s)
        assert cost == 50


    def test_distance_9(self):
        delv = Delivery
        frag = False
        s = 9
        cost = delv.fragility(frag, s)
        assert cost == 100


    def test_distance_10(self):
        delv = Delivery
        frag = False
        s = 10
        cost = delv.fragility(frag, s)
        assert cost == 100

    def test_distance_11(self):
        delv = Delivery
        frag = False
        s = 11
        cost = delv.fragility(frag, s)
        assert cost == 200

    def test_distance_29(self):
        delv = Delivery
        frag = False
        s = 29
        cost = delv.fragility(frag, s)
        assert cost == 200

    def test_distance_30(self):
        delv = Delivery
        frag = False
        s = 30
        cost = delv.fragility(frag, s)
        assert cost == 200

    def test_distance_31(self):
        delv = Delivery
        frag = False
        s = 31
        cost = delv.fragility(frag, s)
        assert cost == 300

    def test_distance_31_frag(self):
        delv = Delivery
        frag = True
        s = 31
        delv.fragility(frag, s)
        assert "Хрупкие товары не могут быть доставлены далее 30 км. Введите другое расстояние."

    # Проверка классов эквивалентности для параметра Размеры
    def test_dimensions_small(self):
        delv = Delivery
        d = "small"
        cost = delv.dimensions(d)
        assert cost == 100

    def test_dimensions_small(self):
        delv = Delivery
        d = "big"
        cost = delv.dimensions(d)
        assert cost == 200

    def test_dimensions_fail(self):
        delv = Delivery
        d = "aaa"
        delv.dimensions(d)
        assert "Данные введены некорректно. Введите big/small."

    # Проверка классов эквивалентности для параметра Загруженность
    def test_workload_vh(self):
        delv = Delivery
        l = "vh"
        cost = delv.workload(l)
        assert cost == 1.6

    def test_workload_h(self):
        delv = Delivery
        l = "h"
        cost = delv.workload(l)
        assert cost == 1.4


    def test_workload_aa(self):
        delv = Delivery
        l = "aa"
        cost = delv.workload(l)
        assert cost == 1.2

    def test_workload_nn(self):
        delv = Delivery
        l = "nn"
        cost = delv.workload(l)
        assert cost == 1


