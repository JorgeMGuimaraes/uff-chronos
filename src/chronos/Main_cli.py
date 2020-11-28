import argparse
from pathlib import Path
from Controle_entidade import ControleEntidade
from Controle_csv import ControleCsv

if __name__ == "__main__":
    parser  = argparse.ArgumentParser(description='Processa um dataset e imprime Crs.')
    parser.add_argument("caminho", type=Path)
    args    = parser.parse_args()
    if not args.caminho.exists():
        print('Este arquivo nao existe. Confirme o caminho e tente novamente.')
        exit()
    
    controle_csv        = ControleCsv()
    controle_entidade   = ControleEntidade()
    dados               = controle_csv.get_dict_dados(args.caminho)
    if len(dados) == 0:
        print('Este arquivo se encontra fora do padrao. Tente outro arquivo.')
        exit()
    
    alunos  = dict()
    cursos  = dict()

    for linha in dados:
        controle_entidade.preenche(alunos, 'MATRICULA', linha)
        controle_entidade.preenche(cursos, 'COD_CURSO', linha)

    controle_entidade.imprime_cli(alunos, '------- O CR dos alunos é: --------')
    controle_entidade.imprime_cli(cursos, '----- Média de CR dos cursos: -----')
