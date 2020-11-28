import unittest
from controle_csv import ControleCsv
from Aluno import Aluno

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

class Teste_Aluno(unittest.TestCase):
    """
    Testa o comportamento do objeto aluno
    """

    def teste_aluno(self):
        aluno = Aluno()
        
        self.assertEqual(aluno.get_matricula(), 100)
        self.assertIsInstance(aluno.get_matricula(), int)

        self.assertEqual(aluno.get_nota_ponderada(), 10)
        self.assertIsInstance(aluno.get_nota_ponderada(), int)

        self.assertEqual(aluno.get_carga_horaria_total(), 10)
        self.assertIsInstance(aluno.get_carga_horaria_total(), int)

        self.assertEqual(aluno.get_cr(), 10)
        self.assertIsInstance(aluno.get_cr(), int)

if __name__ == "__main__":
    suite_csv   = unittest.TestLoader().loadTestsFromTestCase(Teste_Csv)
    suite_aluno = unittest.TestLoader().loadTestsFromTestCase(Teste_Aluno)

    suites = unittest.TestSuite([
        suite_csv,
        suite_aluno
    ])
    unittest.TextTestRunner(verbosity=2).run(suites)