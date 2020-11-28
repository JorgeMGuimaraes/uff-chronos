
class Aluno():
    """
    Guarda informacoes gereais sobre o aluno
    """
    def __init__(self, matricula):
        self.matricula              = matricula
        self.nota_ponderada         = 0
        self.carga_horaria_total    = 0
        return
    
    def get_matricula(self):
        return self.matricula
    
    def set_nota_ponderada(self, nota, carga):
        self.nota_ponderada += nota * carga
        return
    
    def get_nota_ponderada(self):
        return self.nota_ponderada

    def set_carga_horaria_total(self, carga):
        self.carga_horaria_total += carga

    def get_carga_horaria_total(self):
        return self.carga_horaria_total

    def get_cr(self):
        return int(self.nota_ponderada / self.carga_horaria_total)