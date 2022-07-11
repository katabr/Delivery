# ПРоверка проводится отдельными тестами для наглядности прохождения
# Для улучшения автоматизации педлагается проводить тестирование с параметрами
# Тестовые наборы представлены в файле Data

import unittest
import pytest
import allure
import Exception


from ..functions.delivery import Delivery



class TestDelivery(unittest.TestCase, Delivery):
    delv = Delivery


    # Положительные тесты
    def test_full_cost_of_delivery_31(self):
        delv = Delivery
        frag = False
        s = 31
        d = "small"
        l = "vh"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert cost == 800

    def test_full_cost_of_delivery_20(self):
        delv = Delivery
        frag = True
        s = 20
        d = "big"
        l = "h"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert cost == 840

    def test_full_cost_of_delivery_10(self):
        delv = Delivery
        frag = True
        s = 10
        d = "small"
        l = "aa"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert cost == 480

    def test_full_cost_of_delivery_2(self):
        delv = Delivery
        frag = True
        s = 2
        d = "big"
        l = "aa"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert cost == 450


 # Проверка стоимости меньше и равно минимальной
    def test_full_cost_of_delivery_l_400(self):
        delv = Delivery
        frag = False
        s = 0.5
        d = "small"
        l = "nn"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert cost == 400

    def test_full_cost_of_delivery_400(self):
        delv = Delivery
        frag = False
        s = 30
        d = "big"
        l = "nn"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert cost == 400

# Ожидаемо падающие тесты
    @ pytest.xfail()
    def test_full_cost_of_delivery_400(self):
        delv = Delivery
        frag = True
        s = 31
        d = "big"
        l = "vh"
        cost = delv.full_cost_of_delivery(frag, s, d, l)
        assert Exception



