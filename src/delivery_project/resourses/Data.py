# Тестовые наборы

class TestData:
    data = {
            {
            {
                "frag" : False,
                "s" : 31,
                "d" : "small",
                "l" : "vh"
            } : 800
        },
        {
            {
                "frag": True,
                "s": 20,
                "d": "big",
                "l": "h"
            }: 840
        },
        {
            {
                "frag": True,
                "s": 10,
                "d": "small",
                "l": "aa"
            }: 480
        },
        {
                {
                    "frag" : True,
                    "s" : 2,
                    "d" : "big",
                    "l" : "aa"
                } : 450
            },
        {
            {
                "frag": False,
                "s": 0.5,
                "d": "small",
                "l": "nn"
            }: 400
        },
        {
            {
                "frag": False,
                "s": 30,
                "d": "big",
                "l": "nn"
            }: 400
        },

        # Ожидаемо падающие тесты
        {
                {
                    "frag" : True,
                    "s" : 31,
                    "d" : "big",
                    "l" : "vh"
                } : Exception
            }
    }




