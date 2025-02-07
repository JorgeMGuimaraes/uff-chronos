import unittest
from Controle_csv import ControleCsv
from Entidade import Entidade

class Teste_Csv(unittest.TestCase):
    """
    Testa a importação de dados csv
    """
    def teste_carregar_csv(self):
        caminho = 'teste_dados.csv'
        dados   = ControleCsv().get_dict_dados(caminho)
        for linha in dados:
            self.assertEqual(linha['MATRICULA'], '100')
    
    def teste_fora_do_padrao(self):
        caminho = 'falso.csv'
        dados   = ControleCsv().get_dict_dados(caminho)
        self.assertEqual(len(dados), 0)

class Teste_Aluno(unittest.TestCase):
    """
    Testa o comportamento do objeto aluno
    """

    def teste_aluno(self):
        aluno1 = Entidade(100)        
        self.assertEqual(aluno1.id, 100)
        self.assertIsInstance(aluno1.id, int)

        aluno1.set_nota_ponderada(10, 10)
        self.assertEqual(aluno1.nota_ponderada, 100)
        self.assertIsInstance(aluno1.nota_ponderada, int)

        aluno1.set_carga_horaria_total(10)
        self.assertEqual(aluno1.carga_horaria_total, 10)
        self.assertIsInstance(aluno1.carga_horaria_total, int)

        self.assertEqual(aluno1.get_cr(), 10)
        self.assertIsInstance(aluno1.get_cr(), int)

        aluno2  = Entidade(200)
        nota    = 0
        carga   = 0
        aluno2.set_carga_horaria_total(carga)
        aluno2.set_nota_ponderada(nota, carga)
        self.assertEqual(aluno2.get_cr(), 0)

if __name__ == "__main__":
    suite_csv   = unittest.TestLoader().loadTestsFromTestCase(Teste_Csv)
    suite_aluno = unittest.TestLoader().loadTestsFromTestCase(Teste_Aluno)

    suites = unittest.TestSuite([
        suite_csv,
        suite_aluno
    ])
    unittest.TextTestRunner(verbosity=2).run(suites)