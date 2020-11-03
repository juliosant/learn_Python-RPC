from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Citizen:
    def __init__(self, id, name, age, nationality):
        self.id = id
        self.name = name
        self.age = age
        self.nationality = nationality

class City:
    def __init__(self):
        self.citizens =[]
        self.citizens.append(Citizen(id =9783, name ='Matheus', age=18, nationality ='South African'))
        self.citizens.append(Citizen(id =5735, name ='Marcos', age=26, nationality ='Israeli'))
        self.citizens.append(Citizen(id =3759, name ='Lucas', age=28, nationality ='Brasilian'))
        self.citizens.append(Citizen(id =8927, name ='Joao', age=21, nationality ='Irish'))

    def showCitizenById(self, id):
        for citizen in self.citizens:
            if citizen.id == id:
                return f'cidadão nº{citizen.id}:\n Nome: {citizen.name}\n Idade: {citizen.age}\n Nacionalidade: {citizen.nationality}'
        return False
    
    def showCitizenByName(self, name):
        for citizen in self.citizens:
            if citizen.name == name:
                return f'Cidadão nº{citizen.id}:\n Nome: {citizen.name}\n Idade: {citizen.age}\n Nacionalidade: {citizen.nationality}'
        return False
    
    def registerCitizen(self, newId, newName, newAge, newNationality):
        self.citizens.append(Citizen(id =newId, name =newName, age =newAge, nationality =newNationality))
        print(f'Cidadão {newName} foi cadastrado id: {newId}')
        return f'Cidadão {newName} foi cadastrado, id: {newId}'

    def updateCitizen(self, newId, newName, newAge, newNationality):
        for citizen in self.citizens:
            if citizen.id == newId:
                citizen.name = newName
                citizen.age = newAge
                citizen.nationality = newNationality
                print(f'Dados de {citizen.id} - {citizen.name} foram alterados')
                return f'Dados de {citizen.id} - {citizen.name} foram alterados'
        return False
#Criar servidor RCP
with SimpleXMLRPCServer(('localhost', 8001),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()
    
    server.register_instance(City())
    #Servidor em loop
    server.serve_forever()