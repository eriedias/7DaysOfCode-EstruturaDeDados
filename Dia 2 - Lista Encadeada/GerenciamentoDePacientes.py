class Paciente:
    def __init__(self, id, nome, saude):
        self.id = id
        self.nome = nome
        self.saude = saude
        self.proximoPaciente = None

class ListaDePacientes:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def adicionar_paciente(self, id, nome, saude):
        novoPaciente = Paciente(id, nome, saude)
        if self.head is None:
            self.head = novoPaciente
            self.tail = novoPaciente
        else:
            self.tail.proximoPaciente = novoPaciente
            self.tail = novoPaciente

    def remover_paciente(self, id):
        if self.head is None:
            return
        elif self.head.id == id:
            self.head = self.head.proximoPaciente
        if self.head is None: 
            self.tail = None
            return
        else:
            pacienteAtual = self.head
        while pacienteAtual.proximoPaciente is not None:
            if pacienteAtual.proximoPaciente.id == id:
                pacienteAtual.proximoPaciente = pacienteAtual.proximoPaciente.proximoPaciente
            if pacienteAtual.proximoPaciente is None:
                self.tail = pacienteAtual
                return
            pacienteAtual = pacienteAtual.proximoPaciente

    def listar_pacientes(self):
        if self.head is None:
            print('Não há pacientes nesta lista.')
        else:
            pacienteAtual = self.head
            while pacienteAtual is not None:
                print(f"Nome: {pacienteAtual.nome}, ID: {pacienteAtual.id}, Estado de Saúde: {pacienteAtual.saude}")
                pacienteAtual = pacienteAtual.proximoPaciente


listaDePacientes = ListaDePacientes()

listaDePacientes.adicionar_paciente(1, "João", "Estável")
listaDePacientes.adicionar_paciente(2, "Mariana", "Em tratamento")
listaDePacientes.adicionar_paciente(3, "Carla", "Estável")
listaDePacientes.adicionar_paciente(4, "Pedro", "Crítico")

listaDePacientes.listar_pacientes()

print('----- Removendo o pciente de ID 3 -----')
listaDePacientes.remover_paciente(3)

listaDePacientes.listar_pacientes()