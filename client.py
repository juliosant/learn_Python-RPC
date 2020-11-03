import xmlrpc.client
from random import randrange

s = xmlrpc.client.ServerProxy('http://localhost:8000')

#print('Localizar Paciente com id 5735...')
#print(s.showPacientById(5735))

#print('Cadastrar novo paciente...')
#print(s.registerPacient(7985, 'Paulo', 31, 'French'))
#print('Localizar Paciente com id 7985...')
#print(s.showPacientById(7985))
#print(s.registerPacient(3978, 'Joana', 33, 'England'))
#print('Localizar Paciente com id 3978...')
#print(s.showPacientById(3978))

print("-----------------HOSPITAL CENTRAL-----------------")
print('--------------ATENDIMENTO AO CLIENTE--------------')
op = int(input("""ESCOLHA UM DE NOSSOS ATENDIMENTOS:
            [1] CONSULTAR
            [2] CADASTRAR
            [3] ATUALIZAR
            [4] DAR ALTA
            [5] SAIR
            """
            ))

if op == 1:
    while True:
        choice = str(input("""BUSCAR POR: 
        [N] NOME
        [I] ID
        [Q] PARA SAIR
        """
        )).upper()
        if choice == 'I':
            id = int(input('INFORME O ID DO PACIENTE: '))
            print(s.showPacientById(id))
        elif choice == 'N':
            name = str(input('INFORME O NOME DO PACIENTE: '))
            print(s.showPacientByName(name))
        elif choice == 'Q':
            break
        else:
            print('OOPÇÃO INVÁLIDA.')

elif op == 2:
    choice = 'S'
    while True:
        if choice == 'S':
            id = randrange(1000, 9999)
            name = str(input('NOME: ')).title()
            age = int(input('IDADE: '))
            nationality = str(input('NACIONALIDADE: ')).title()
            print(s.registerPacient(id, name, age, nationality))

            choice = str(input("VOCÊ DESEJA CADASTRAR NOVO PACIENTE?(S/N): ")).upper()
        elif choice == 'N':
            print('OBRIGADO!')
            break
        else:
            print('OOPÇÃO INVÁLIDA.')
            choice = str(input("VOCÊ DESEJA CADASTRAR NOVO PACIENTE?(S/N): ")).upper()

elif op == 3:
    id = int(input('ID: '))
    name = str(input('NOME: '))
    age = int(input('IDADE: '))
    nationality = str(input('NACIONALIDADE: '))

    print(s.updatePacient(id, name, age, nationality))

elif op == 4:
    print('Em construção')
elif op == 5:
    print('Em construção')
else:
    print('Opção inválida')