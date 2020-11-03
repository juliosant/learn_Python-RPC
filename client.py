import xmlrpc.client
from random import randrange

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print('Localizar Paciente com id 5735...')
print(s.showPacientById(5735))

#print('Cadastrar novo paciente...')
#print(s.registerPacient(7985, 'Paulo', 31, 'French'))
#print('Localizar Paciente com id 7985...')
#print(s.showPacientById(7985))
#print(s.registerPacient(3978, 'Joana', 33, 'England'))
#print('Localizar Paciente com id 3978...')
#print(s.showPacientById(3978))

print("-----------HOSPITAL PASSO PARA O INFERNO-----------")
op = str(input("Você deseja cadastrar novo paciente(S/N))")).upper()

while True:
    if op == 'N':
        print('Obrigado!')
        break
    elif op == 'S':
        id = randrange(1000, 9999)
        name = str(input('Nome: ')).title()
        age = int(input('Idade: '))
        nationality = str(input('Nacionalidade: ')).title()
        print(s.registerPacient(id, name, age, nationality))

        op = str(input("Você deseja cadastrar novo paciente(S/N))")).upper()

    else:
        print('Opção inválida. Tente novamente.')
        op = str(input("Você deseja cadastrar novo paciente(S/N))")).upper()
