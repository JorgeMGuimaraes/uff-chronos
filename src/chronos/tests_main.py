import unittest
from controle_csv import *

class Teste_Csv(unittest.TestCase):
    """
    Testa a importação de dados csv
    """
    def teste_carregar_csv(self):
        caminho = 'teste_dados.csv'
        dados   = ControleCsv().get_dict_dados(caminho)
        for linha in resp:
            resp = linha
        self.assertEqual(resp['MATRICULA'] == 100)


if __name__ == "__main__":
    unittest.main()