from Controle_csv import ControleCsv
from Entidade import Entidade

class ControleEntidade():
    """
    Opera e manipula entidades que contem CR
    """
    
    def preenche(self, meu_dict:dict, tipo_id:str, lin:dict)-> None:
        '''
        Preenche os campos da 'Entidade' com os dados do dataset.
        Parameters
        ----------
        meu_dict : dict
            Estrutura que guarda entidades semelhantes.
        tipo_id : str
            Identificador proprio do tipo de entrada:
            Ex.:    estudantes -> matricula
                    curso -> id_curso
        lin : dict
            Estrutura que contem os dados vindos do dataset, parseado por 
            get_dict_dados de alguma classe que a implemente.

        '''
        id      = int(lin[tipo_id])
        carga   = int(lin['CARGA_HORARIA'])
        nota    = int(lin['NOTA'])

        if not id in meu_dict.keys():
            elem            = Entidade(id)
            meu_dict[id]    = elem
        
        meu_dict[id].set_carga_horaria_total(carga)
        meu_dict[id].set_nota_ponderada(nota, carga)
        return

    def imprime_cli(self, meu_dict:dict, msg:str)-> None:
        '''
        Imprime para o terminal as informacoes de cr de cada tipo de entidade.
        Parameters
        ----------
        meu_dict : dict
            Estrutura que guarda entidades semelhantes.
        msg : str
            Cabecalho, ou outra informacao qualquer a ser impressa antes da lista 
            de resultados.
        '''
        print(msg)
        for _, val in sorted(meu_dict.items()):
            print(val.get_output_cr())
        print('-----------------------------------\n')
        return
