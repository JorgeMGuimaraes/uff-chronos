import unittest
from controle_csv import ControleCsv

class Teste_Csv(unittest.TestCase):
    """
    Testa a importação de dados csv
    """
    def teste_carregar_csv(self):
        caminho = 'teste_dados.csv'
        dados   = ControleCsv().get_dict_dados(caminho)
        for linha in dados:
            self.assertEqual(linha['MATRICULA'], '100')
    
    def teste_falhar_csv(self):
        caminho = 'nada.csv'
        dados   = ControleCsv().get_dict_dados(caminho)
        for linha in dados:
            self.assertTrue('erro' in linha.keys())

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Teste_Csv)
    unittest.TextTestRunner(verbosity=2).run(suite)