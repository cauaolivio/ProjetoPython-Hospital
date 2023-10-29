def menu():
	print("MENU DE OPÇÕES")
	print("1. Submenu de Médicos")
	print("2. Submenu de Pacientes")
	print("3. Submenu de Consultas")
	print("4. Submenu dos Relatórios")
	print("5. Sair")

	opc = int(input("Qual opção você deseja? "))

	return opc

# DICIONÁRIO DOS MÉDICOS
def inserirMedicos(medicos, emails, telefones):
    crm = str(input("Digite o CRM: ")).lower()
    if verificarInclusao(medicos, crm):
        nome = str(input("Digite o seu nome: ")).lower()
        data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
        sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
        especialidade = str(input("Digite a sua especialidade: ")).lower()
        universidade = str(input("Digite a universidade em que se formou: ")).lower()

        emails = inserirEmail(emails)
        telefones = inserirTelefones(telefones)

        medicos [crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]

        return True
    else:
        return False

def alterarMedico(medicos):
    return True

def excluirMedico(medicos):
    return True

def listarMedico(medicos):
    return True



# DICIONÁRIO DOS PACIENTES

def inserirPacientes(pacientes, emails, telefones):
    cpf = str(input("Digite o CPF: ")).lower()
    if verificarInclusao(pacientes, cpf):
        nome = str(input("Digite o seu nome: ")).lower()
        data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
        sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
        plano_saude = str(input("Digite o seu plano de saúde: ")).lower()
        emails = inserirEmail(emails)
        telefones = inserirTelefones(telefones)

        pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
        return True
    else:
        print("Paciente já está na lista")

        return False

def alterarPaciente(pacientes):
    return True

def excluirPaciente(pacientes):
    cpf = str(input("Infome o cpf do paciente que deseja excluir: "))
    if cpf in pacientes.keys():
        del pacientes[cpf]
        return True
    else:
        return False

def listarPaciente(pacientes):
    return True

def listarTodos(dicionario): #Utilizado para pacientes, medicos e consultas
    return True


# DICIONÁRIO DA CONSULTA
# Consulta = (CRM, CPF, Data, Hora, Diagnostico, Medicamentos)
def inserirConsultas(consultas):
    crm = str(input("Digite o CRM: ")).lower()
    cpf = str(input("Digite o CPF: ")).lower()
    data = str(input("Digite a data (xx/xx/xxxx): ")).lower()
    hora = str(input("Digite o horario (xx:xx): ")).lower()
    chaves = (crm, cpf, data, hora)
    if verificarInclusao(consultas, chaves):
        diagnostico = str(input("Digite o diagnostico: ")).lower()
        medicamentos = []
        medicamentos = inserirMedicamentos(medicamentos)
        consultas[chaves] = [diagnostico, medicamentos]
        return True
    else:
        return False

def alterarConsulta(consultas):
    return True

def excluirConsulta(consultas):
    return True

def listarConsulta(consultas):
    return True

def medicosEspecilizacaoX(medicos,especializacao):
    return True

def pacientesMenoresXIdade(pacientes,idade):
    return True

def mostrarConsultasNosUltimosXDias(medicos, pacientes, consultas, diasAtras):
    return True
# SUBFUNÇÕES
def inserirEmail(emails):
    email = str(input("Digite o e-mail: ")).lower()
    
    while email != "":
        emails.append(email)
        email = str(input("Digite o e-mail ou [ENTER] para sair: ")).lower()
    
    return emails
        

def inserirTelefones(telefones):
    telefone = str(input("Digite o telefone ou [ENTER] para sair: ")).lower()

    while telefone != "":
        telefones.append(telefone)
        telefone = str(input("Digite o telefone ou [ENTER] para sair: ")).lower()
    
    return telefones

def inserirMedicamentos(medicamentos):
    medicamento = str(input("Digite o medicamento: ")).lower()
    
    while medicamento != "":
        medicamentos.append(medicamento)
        medicamento = str(input("Digite o medicamento ou [ENTER] para sair: ")).lower()

    return medicamentos

def verificarInclusao(dicionario, chave):
    if chave not in dicionario.keys():
        return True
    else:
        return False

# FUNÇÕES PRINCIPAIS
def subMenu(opcao, medicos, pacientes, consultas):
    while opcao <= 4:
        emails = []
        telefones = []
        print("="*100)
        print("SUBMENU DE OPÇÕES")
        if opcao == 1:
            print("1. Incluir Médico")
            print("2. Alterar Médico")
            print("3. Excluir Médico")
            print("4. Listar Médico")
            print("5. Listar Todos")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirMedicos(medicos, emails, telefones):
                    print("Médico adicionado com sucesso!")
                else:
                    print("Médico já está cadastrado")

        elif opcao == 2:
            print("1. Incluir Paciente")
            print("2. Alterar Paciente")
            print("3. Excluir Paciente")
            print("4. Listar Paciente")
            print("5. Listar Todos")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirPacientes(pacientes, emails, telefones):
                    print("Paciente adicionado com sucesso!")
                else:
                    print("Paciente já esta cadastrado")
            
            elif opc ==3:
                if excluirPaciente(pacientes):
                    print("Paciente excluido com sucesso!")
                else:
                    print("Paciente não cadastrado")

        elif opcao == 3:
            print("1. Incluir Consulta")
            print("2. Alterar Consulta")
            print("3. Excluir Consulta")
            print("4. Listar Consulta")
            print("5. Listar Todas")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirConsultas(consultas):
                    print("Consulta marcada com sucesso!")
                else:
                    print("Consulta não marcada!")

        elif opcao == 4:
            print("1. Mostrar medicos com a especialização X")
            print("2. Mostrar pacientes menores de X idade")
            print("3. Mostrar o CRM, o nome do médico, o CPF do paciente, o nome do paciente, data, hora, diagnostico e medicamentos para todas as consultas realizadasnos últimos X dias")
            opc = int(input("Qual opção você deseja? "))   

            if opc == 1:
                especializacao = str(input("Informe a especialização desejada: "))
                if medicosEspecilizacaoX(medicos,especializacao):
                    print(f"Esses são os médicos com a especialização {especializacao} !")
                else:
                    print(f"Não temos médicos com a especialização informada {especializacao}")
            elif opc == 2:
                idade = int(input("Informe a idade máxima dos pacientes que deseja ver: "))
                if pacientesMenoresXIdade(pacientes, idade):
                    print(f"Esses são os pacientes menores de {idade} anos!")
                else:
                    print(f"Não temos pacientes menores de {idade} anos!")
            elif opc == 3:
                ultimosDias = int(input("Informe de quantos dias atrás deseja ver consultas: "))
                if mostrarConsultasNosUltimosXDias(medicos, pacientes, consultas):
                    print(f"Essas são as consultas dos ultimos {ultimosDias} dias ")
                
        print("="*100)
        opcao = menu()
        
    print("Encerrando...")    

def main():
    medicos = dict()
    pacientes = dict()
    consultas = dict()

    subMenu(menu(), medicos, pacientes, consultas)

    print(medicos)
    print(pacientes)
    print(consultas)
    
    
main()