# -*- coding: utf-8 -*-
class Calculator:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b == 0:
            return "Denominator cannot be zero"
        return a / b
