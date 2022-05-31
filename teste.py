from cgitb import reset
import os
from click import getchar
from Pessoa import Pessoa

# para '__true = True' qualquer 'symbols' dentro de 'nome' = falha
# para '__true = False' o 'nome' tem que estar contido em 'symbols'
def Validate(nome, symbols, __true):
    verificador = True
    for i in range(nome.__len__()):
        if not __true:
            if not verificador:
                return False
            verificador = False
        for j in range(symbols.__len__()):
            if __true:
                if (nome[i] == symbols[j]):
                    return False
            if not __true:
                if (nome[i] == symbols[j]):
                    verificador = True
    return True

def printCadastro (indexador):
    os.system("clear")
    print('Digite o nome.')
    if indexador == 0:
        return
    print(NewPerson.Nome)
    if indexador == 1:
        return
    print('Digite a idade.')
    if indexador == 2:
        return
    print(NewPerson.Idade)
    if indexador == 3:
        return
    print('Digite o endereço.')
    if indexador == 4:
        return
    print(NewPerson.Endereco)
    if indexador == 5:
        return
    print('Digite o telefone.')
    if indexador == 6:
        return
    print(NewPerson.Telefone)
    if indexador == 7:
        return
    print('Digite o sexo. "h" para homem, "m" para mulher')
    if indexador == 8:
        return
    print(NewPerson.Sexo)
    if indexador == 9:
        return
    print('Digite a profissão.')
    if indexador == 10:
        return
    print(NewPerson.Profissao)
    
os.system("clear")
guilherme = 'superman'
print (guilherme)
if not os.path.exists('./cadastros/'):
    os.mkdir('./cadastros')
choice = 0

RED = '\033[31m'
RESET = '\033[0;0m'

while choice != 3:
    try:
        choice = int(input('Digite 1 para adicionar dados, 2 para ver dados salvos, e 3 para sair.\n'))
    except ValueError:
        os.system("clear")
        continue
    os.system("clear")
    if choice == 1:
    
        NewPerson = Pessoa()
        
        printCadastro(0)
        while True:
            NewPerson.Nome = input()
            if not Validate(NewPerson.Nome, "!@#$%*()-_=+[}{]~^'`,<.>;:/?\|*1234567890", True):
                printCadastro(1)
                print( RED + "Digite um nome valido" + RESET)
                continue
            break
        
        printCadastro(2)        
        while True:
            NewPerson.Idade = input()
            try:
                NewPerson.Idade = int(NewPerson.Idade)
            except:
                printCadastro(3)
                print(RED +'Porfavor use digitos numéricos.'+ RESET)
                continue
            if NewPerson.Idade < 1 or NewPerson.Idade >150:
                printCadastro(3)
                print(RED +'Porfavor digite um número positivo menor que 150'+ RESET)
                continue
            NewPerson.Idade = str(NewPerson.Idade)
            break
        printCadastro(4)
        while True:
            NewPerson.Endereco = input()
            if not Validate(NewPerson.Endereco, "!@#$%*()_=+[}{]~^'`<.>;/?\|*", True):
                printCadastro(5)
                print(RED +"Digite um endereço valido"+ RESET)
                continue
            break
        printCadastro(6)
        while True:
            NewPerson.Telefone = input()
            if not Validate(NewPerson.Telefone, "1234567890+() ", False):
                printCadastro(7)
                print(RED +"Digite um telefone valido"+ RESET)
                continue
            break
        printCadastro(8)
        while True:
            NewPerson.Sexo = input()
            if NewPerson.Sexo == 'h' or NewPerson.Sexo == 'm':
                break
            printCadastro(9)
            print(RED +"apenas 'h' e 'm' são aceitos"+ RESET)
        printCadastro(10)
        while True:
            NewPerson.Profissao = input()
            if not Validate(NewPerson.Profissao, "!@#$%*()-_=+[}{]~^'`,<.>;:/?\|*1234567890", True):
                printCadastro(11)
                print(RED +"Digite uma profissão valida"+ RESET)
                NewPerson.Profissao = ''
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