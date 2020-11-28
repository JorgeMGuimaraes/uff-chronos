
class Entidade():
    """
    Guarda informacoes gereais sobre o aluno
    """
    def __init__(self, id):
        self.id                     = id
        self.nota_ponderada         = 0
        self.carga_horaria_total    = 0
        return
       
    def set_nota_ponderada(self, nota, carga):
        self.nota_ponderada += nota * carga
        return
    
    def set_carga_horaria_total(self, carga):
        self.carga_horaria_total += carga

    def get_cr(self):
        if self.carga_horaria_total == 0:
            return 0
        return int(self.nota_ponderada / self.carga_horaria_total)
    
    def get_output_cr(self):
        return '{0}\t-  {1}'.format(self.id, self.get_cr())