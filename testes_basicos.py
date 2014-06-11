# -*- coding: utf-8 -*-
import unittest

def soma(param1, param2):
    return param1 + param2

class BasicoTests(unittest.TestCase):
    def soma_test(self):
        resultado = soma(1,2)
        self.assertEqual(3,resultado)