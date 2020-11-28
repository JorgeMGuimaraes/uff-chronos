import csv

class ControleCsv():
    """
    Opera e manipula dados csv
    """
    
    def get_dict_dados(self, caminho):
        try:
            lista_de_dados = []
            with open(caminho, newline='') as arquivo_csv:

                cabecalho = 'MATRICULA,COD_DISCIPLINA,COD_CURSO,NOTA,CARGA_HORARIA,ANO_SEMESTRE' 
                if not cabecalho in arquivo_csv.readline():
                    return lista_de_dados

                arquivo_csv.seek(0)
                dados = csv.DictReader(arquivo_csv)
                for linha in dados:
                    lista_de_dados.append(linha)
            return lista_de_dados

        except IOError:
            lista_de_dados.append({'erro':'arquivo nao encontrado'})
            return lista_de_dados