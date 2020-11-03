import xmlrpc.client
from random import randrange

s = xmlrpc.client.ServerProxy('http://localhost:8001')

#print('Localizar Cidadão com id 5735...')
#print(s.showCitizentById(5735))

#print('Cadastrar novo cidadão...')
#print(s.registerCitizen(7985, 'Paulo', 31, 'French'))
#print('Localizar Cidadão com id 7985...')
#print(s.showCitizenById(7985))
#print(s.registerCitizen(3978, 'Joana', 33, 'England'))
#print('Localizar Cidadão com id 3978...')
#print(s.showCitizentById(3978))

print("------------------CIDADE CENTRAL------------------")
print('--------------ATENDIMENTO AO CLIENTE--------------')
op = int(input("""ESCOLHA UM DE NOSSOS ATENDIMENTOS:
            [1] CONSULTAR CIDADÃO
            [2] CADASTRAR CIDADÃO
            [3] ATUALIZAR CIDADÃO
            [4] EXCLUIR CIDADÃO
            [5] SAIR DO ATENDIMENTO
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
            id = int(input('INFORME O ID DO CIDADÃO: '))
            print(s.showCitizenById(id))
        elif choice == 'N':
            name = str(input('INFORME O NOME DO CIDADÃO: '))
            print(s.showCitizenByName(name))
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
            print(s.registerCitizen(id, name, age, nationality))

            choice = str(input("VOCÊ DESEJA CADASTRAR NOVO CIDADÃO?(S/N): ")).upper()
        elif choice == 'N':
            print('OBRIGADO!')
            break
        else:
            print('OOPÇÃO INVÁLIDA.')
            choice = str(input("VOCÊ DESEJA CADASTRAR NOVO CIDADÃO?(S/N): ")).upper()

elif op == 3:
    id = int(input('ID: '))
    name = str(input('NOME: '))
    age = int(input('IDADE: '))
    nationality = str(input('NACIONALIDADE: '))

    print(s.updateCitizen(id, name, age, nationality))

elif op == 4:
    print('Em construção')
elif op == 5:
    print('Em construção')
else:
    print('Opção inválida')