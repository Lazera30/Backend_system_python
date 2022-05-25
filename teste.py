import os
from click import getchar
from Pessoa import Pessoa

def Validate(nome, symbols, __not):
    for i in range(nome.__len__()):
        for j in range(symbols.__len__()):
            if (nome[i] == symbols[j]) and __not:
                return False
    return True

os.system("clear")
if not os.path.exists('./cadastros/'):
    os.mkdir('./cadastros')
choice = 0
while choice != 3:
    choice = int(input('Digite 1 para adicionar dados, 2 para ver dados salvos, e para sair.\n'))
    os.system("clear")
    if choice == 1:
        NewPerson = Pessoa()
        
        while True:
            NewPerson.Nome = input('Digite o nome.\n')
            if not Validate(NewPerson.Nome, "!@#$%*()-_=+[}{]~^'`,<.>;:/?\|*1234567890", True):
                print("Digite um nome valido")
                continue
            break
                
        while True:
            NewPerson.Idade = input('Digite a idade.\n')
            try:
                NewPerson.Idade = int(NewPerson.Idade)
            except:
                print('Porfavor use digitos numéricos.')
                continue
            if NewPerson.Idade < 1 and NewPerson.Idade <150:
                print('Porfavor digite um número positivo menor que 150')
                continue
            NewPerson.Idade = str(NewPerson.Idade)
            break
               
        while True:
            NewPerson.Endereco = input('Digite o endereço.\n')
            if not Validate(NewPerson.Endereco, "!@#$%*()_=+[}{]~^'`<.>;/?\|*", True):
                print("Digite um endereço valido")
                continue
            break
        
        while True:
            NewPerson.Telefone = input('Digite o telefone.\n')
            if not Validate(NewPerson.Telefone, "1234567890+() ", False):
                print("Digite um telefone valido")
                continue
            break
        
        while True:
            NewPerson.Sexo = input('Digite o sexo. "h" para homem, "m" para mulher\n')
            if NewPerson.Sexo == 'h' or NewPerson.Sexo == 'm':
                break
        
        while True:
            NewPerson.Profissao = input('Digite a profissão.\n')
            if not Validate(NewPerson.Profissao, "!@#$%*()-_=+[}{]~^'`,<.>;:/?\|*1234567890", True):
                print("Digite uma profissão valida")
                continue
            break
        
        
        fd = open('./cadastros/bd-teste.txt', 'a')
        string = NewPerson.Nome + "\n" + NewPerson.Idade + "\n" + NewPerson.Endereco + "\n" + NewPerson.Telefone + "\n" + NewPerson.Sexo + "\n" + NewPerson.Profissao + "\n"
        fd.write(string)
        fd.close()
        os.system("clear")
    if choice == 2:
        fd = open('./cadastros/bd-teste.txt', 'r')
        line = fd.read()
        indexLine = line.split('\n')
        i=0
        len = indexLine.__len__() - 1
        while i < len:
            print("Nome: " + indexLine[i])
            print("Idade: " + indexLine[i+1])
            print("Endereço: " + indexLine[i+2])
            print("Telefone: " + indexLine[i+3])    
            print("Sexo: " + indexLine[i+4])
            print("Profissão: " + indexLine[i+5] + '\n')
            i = i + 6
        fd.close()
        getchar()
        os.system("clear")