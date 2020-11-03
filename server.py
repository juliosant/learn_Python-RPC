from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Pacient:
    def __init__(self, id, name, age, nationality):
        self.id = id
        self.name = name
        self.age = age
        self.nationality = nationality

class Hospital:
    def __init__(self):
        self.pacients =[]
        self.pacients.append(Pacient(id =9783, name ='Matheus', age=18, nationality ='South African'))
        self.pacients.append(Pacient(id =5735, name ='Marcos', age=26, nationality ='Israeli'))
        self.pacients.append(Pacient(id =3759, name ='Lucas', age=28, nationality ='Brasilian'))
        self.pacients.append(Pacient(id =8927, name ='Joao', age=21, nationality ='Irish'))

    def showPacientById(self, id):
        for pacient in self.pacients:
            if pacient.id == id:
                return f'Paciente nº{id}:\n Nome: {pacient.name}\n Idade: {pacient.age}\n Nacionalidade: {pacient.nationality}'
        return False
    
    def registerPacient(self, newId, newName, newAge, newNationality):
        self.pacients.append(Pacient(id =newId, name =newName, age =newAge, nationality =newNationality))
        print(f'Paciente {newName} foi cadastrado id: {newId}')
        return f'Paciente {newName} foi cadastrado, id: {newId}'
#Criar servidor RCP
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()
    
    server.register_instance(Hospital())
    #Servidor em loop
    server.serve_forever()