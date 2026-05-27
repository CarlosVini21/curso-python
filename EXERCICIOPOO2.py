class Turma:
    def __init__(self,quantAlunos,materias,horarios):
        self.quantAlunos = quantAlunos
        self.materias = materias
        self.horarios = horarios
        
    

    def apresentaTurma(self):
        print(f"A quantidade de alunos é {self.quantAlunos}, "
              f"tenho essa matéria {self.materias}, "
              f"nesse horário {self.horarios}")


turma1 = Turma(20,"Programação","20:30" )
turma1.apresentaTurma()
