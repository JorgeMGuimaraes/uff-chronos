
class Entidade():
    """
    Guarda informacoes gerais sobre o aluno.
    """
    def __init__(self, id: int):
        '''
        Guarda informacoes gerais sobre o aluno.
        '''
        self.id                     = id
        self.nota_ponderada         = 0
        self.carga_horaria_total    = 0
        return
       
    def set_nota_ponderada(self, nota: int, carga: int)-> None:
        '''
        Incrementa a soma dos produtos 'nota'*'carga horaria'.
        Parameters
        ----------
        nota : int
            A nota atribuida a entidade.
        carga : int
            A carga horaria atribuida a cada curso.
        '''
        self.nota_ponderada += nota * carga
        return
    
    def set_carga_horaria_total(self, carga:int)-> None:
        '''
        Incrementa a carga horaria total da entidade.
        Parameters
        ----------
        carga : int
            A carga horaria atribuida a cada curso.
        '''
        self.carga_horaria_total += carga

    def get_cr(self)-> None:
        '''
        Retorna o CR de cada entidade de acordo com os criterios da universidade
        '''
        if self.carga_horaria_total == 0:
            return 0
        return int(self.nota_ponderada / self.carga_horaria_total)
    
    def get_output_cr(self)-> int:
        '''
        Retorna string formatada com o CR e o id da entidade, como *.ToString()
        '''
        return '{0}\t-  {1}'.format(self.id, self.get_cr())