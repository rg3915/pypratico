import unittest

def sao_anagramas(frase1, frase2):
    """
    Função que identifica anagramas
    :param frase1:
    :param frase2:
    :return: True se frase1 e frase2 são anagramas e False caso contrário
    """

    # eliminar espacos em branco
    frase1 = frase1.replace(' ', '')
    frase2 = frase2.replace(' ', '')

    # comparar tamanho de cadeia com letras. Se for diferente, não são anagramas
    if len(frase1) != len(frase2):
        return False

    # remover cada letra de frase1 e frase2
    for letra_de_1 in frase1:
        frase2 = frase2.replace(letra_de_1, '', 1)

    return len(frase2) == 0

class AnagramaTests(unittest.TestCase):
    def anagramas_test(self):
        self.assertTrue(sao_anagramas('aba', 'baa'))
        self.assertTrue(sao_anagramas('aba', 'aba'))
        self.assertTrue(sao_anagramas('the alias men', 'alan smithee'))

    def nao_anagramas_test(self):
        self.assertFalse(sao_anagramas('not the alias men', 'alan smithee'))
        self.assertFalse(sao_anagramas('aba', 'abap'))
        self.assertFalse(sao_anagramas('aba', 'abb'))