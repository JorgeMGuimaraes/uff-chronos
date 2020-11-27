import csv

class ControleCsv():
    """
    Opera e manipula dados csv
    """
    
    def get_dict_dados(self, caminho):
        lista_de_dados = []
        with open(caminho, newline='') as arquivo_csv:
            dados = csv.DictReader(arquivo_csv)
            for linha in dados:
                lista_de_dados.append(linha)
        return lista_de_dados