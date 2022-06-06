from cgitb import reset
from fileinput import close
import os
from turtle import clear
from venv import create
from wsgiref import validate
from click import getchar
from Pessoa import Pessoa



ATRIBUTOSPESSOA = 8
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

def PrintUpdate(lstUpdate):
    for i in range(int((lstUpdate.__len__())/ATRIBUTOSPESSOA)):
                print(lstUpdate[ATRIBUTOSPESSOA*i].strip('\n') + ') ' + lstUpdate[ATRIBUTOSPESSOA*i + 1].strip('\n'))

def FindRegById(lstUpdate):
    print('Digite o Id do cadastro.')
    for i in range(int((lstUpdate.__len__())/ATRIBUTOSPESSOA)):
        print(lstUpdate[ATRIBUTOSPESSOA*i].strip('\n') + ') ' + lstUpdate[ATRIBUTOSPESSOA*i + 1].strip('\n'))
    while True:
        gui = input()
        if not Validate(gui, '0123456789', False):
            print('Digite o Id do cadastro.')
            for i in range(int((lstUpdate.__len__())/ATRIBUTOSPESSOA)):
                print(lstUpdate[ATRIBUTOSPESSOA*i].strip('\n') + ') ' + lstUpdate[ATRIBUTOSPESSOA*i + 1].strip('\n'))
            print(gui + RED + '\nApenas números são aceitos.' + RESET)
        for i in range(int((lstUpdate.__len__())/ATRIBUTOSPESSOA)):
            if gui == lstUpdate[ATRIBUTOSPESSOA*i].strip('\n'):
                return i
        print(RED + 'Id não encontrado, tente outro' + RESET)
                          
def PrintUpdatePessoa(lstUpdate):
    lstUpdate = Pessoa    
    os.system("clear")
    print('Digite o número correspondente ao campo que quer mudar')
    print('1) Nome: ' + lstUpdate.Nome)
    print('2) Idade: ' + lstUpdate.Idade)
    print('3) Endereço: ' + lstUpdate.Endereco)
    print('4) Telefone: ' + lstUpdate.Telefone)
    print('5) Sexo: ' + lstUpdate.Sexo)
    print('6) Profissão: ' + lstUpdate.Profissao)
    print('7) Email: ' + lstUpdate.Email)
    
def PrintDeletePessoa(lstUpdate):
    lstUpdate = Pessoa    
    os.system("clear")
    print(RED + 'Tem certeza que deseja DELETAR esse cadastro?(s/n)' + RESET)
    print('Nome:        ' + lstUpdate.Nome)
    print('Idade:       ' + lstUpdate.Idade)
    print('Endereço:    ' + lstUpdate.Endereco)
    print('Telefone:    ' + lstUpdate.Telefone)
    print('Sexo:        ' + lstUpdate.Sexo)
    print('Profissão:   ' + lstUpdate.Profissao)
    print('Email:       ' + lstUpdate.Email)
               
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
    if indexador == 11:
        return
    print('Digite o email.')
    if indexador == 12:
        return
    print(NewPerson.Email)
   
os.system("clear")
guilherme = 'superman'
print (guilherme)
if not os.path.exists('./cadastros/'):
    os.mkdir('./cadastros')
choice = 0

RED = '\033[31m'
RESET = '\033[0;0m'

while choice != 5:
    print('Digite 1 para adicionar dados, 2 para ver dados salvos, 3 para atualizar, 4 para deletar, 5 para sair.')
    try:
        choice = int(getchar())
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
        
        printCadastro(12)
        while True:
            NewPerson.Email = input()
            if not Validate(NewPerson.Email, "!#$%*()-=+[}{]~^'`,<>;:/?\|*", True):
                printCadastro(13)
                print(RED +"Digite um email valido"+ RESET)
                NewPerson.Email = ''
                continue
            break
        
        try:        
            fd = open('./cadastros/bd-id.txt', 'r')
        except FileNotFoundError:
            fd = open('./cadastros/bd-id.txt', 'a')
            fd.write('0')
            fd.close()
            fd = open('./cadastros/bd-id.txt', 'r')
            
        idPlus = fd.readlines()
        idPlus[0] = str(int(idPlus[0])+1)
        print(idPlus)
        fd.close()
        fd = open('./cadastros/bd-id.txt', 'w')
        fd.write(idPlus[0])
        fd.close()
        fd = open('./cadastros/bd-teste.txt', 'a')
        string = idPlus[0] + "\n" + NewPerson.Nome + "\n" + NewPerson.Idade + "\n" + NewPerson.Endereco + "\n" + NewPerson.Telefone + "\n" + NewPerson.Sexo + "\n" + NewPerson.Profissao + "\n" + NewPerson.Email + "\n"
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
            print("ID: " + indexLine[i])
            print("Nome: " + indexLine[i+1])
            print("Idade: " + indexLine[i+2])
            print("Endereço: " + indexLine[i+3])
            print("Telefone: " + indexLine[i+4])    
            print("Sexo: " + indexLine[i+5])
            print("Profissão: " + indexLine[i+6])
            print("Email: " + indexLine[i+7] + '\n')
            i = i + ATRIBUTOSPESSOA
            
        fd.close()
        print('Digite qualquer coisa para voltar ao menu inicial.')
        getchar()
        os.system("clear")
        
    if choice == 3: #update
        fd = open('./cadastros/bd-teste.txt', 'r')
        lstCadastroLines = fd.readlines()
        fd.close()
        updateIndex = FindRegById(lstCadastroLines)
        updateIndex = updateIndex*ATRIBUTOSPESSOA
        updatePerson = Pessoa
        updatePerson.Id = lstCadastroLines[updateIndex]
        updatePerson.Nome = lstCadastroLines[updateIndex + 1].strip('\n')
        updatePerson.Idade = lstCadastroLines[updateIndex + 2].strip('\n')
        updatePerson.Endereco = lstCadastroLines[updateIndex + 3].strip('\n')
        updatePerson.Telefone = lstCadastroLines[updateIndex + 4].strip('\n')
        updatePerson.Sexo = lstCadastroLines[updateIndex + 5].strip('\n')
        updatePerson.Profissao = lstCadastroLines[updateIndex + 6].strip('\n')
        updatePerson.Email = lstCadastroLines[updateIndex + 7].strip('\n')
        PrintUpdatePessoa(updatePerson)
        while True:
            upi = input('\n')
            os.system("clear")
            if not Validate(upi, "013456789", False) or int(upi) < 1 or int(upi) > ATRIBUTOSPESSOA:
                PrintUpdate(updatePerson)
                print(RED +'Digite um número entre 1 e ' + ATRIBUTOSPESSOA + RESET)
                continue
            upi = int(upi)
            if upi == 1:
                print('Digite o nome.')
                while True:
                    updatePerson.Nome = input()
                    if not Validate(updatePerson.Nome, "!@#$%*()-_=+[}{]~^'`,<.>;:/?\|*1234567890", True):
                        os.system("clear")
                        print( RED + "Digite um nome valido" + RESET)
                        continue
                    break
                
            if upi == 2:
                print('Digite a idade.')
                while True:
                    updatePerson.Idade = input()
                    os.system("clear")
                    try:
                        updatePerson.Idade = int(updatePerson.Idade)
                    except:
                        print('Digite a idade.\n' + updatePerson.Idade)
                        print(RED +'Porfavor use digitos numéricos.'+ RESET)
                        continue
                    if updatePerson.Idade < 1 or updatePerson.Idade >150:
                        print('Digite a idade.\n', updatePerson.Idade)
                        print(RED +'Porfavor digite um número positivo menor que 150'+ RESET)
                        continue
                    updatePerson.Idade = str(updatePerson.Idade)
                    break
                
            if upi == 3:
                print('Digite o endereço.')
                while True:
                    updatePerson.Endereco = input()
                    if not Validate(updatePerson.Endereco, "!@#$%*()_=+[}{]~^'`<.>;/?\|*", True):
                        print('Digite o endereço.\n' + updatePerson.Endereco)
                        print(RED +"Digite um endereço valido"+ RESET)
                        continue
                    break
                
            if upi == 4:
                print('Digite o telefone.')
                while True:
                    updatePerson.Telefone = input()
                    if not Validate(updatePerson.Telefone, "1234567890+() ", False):
                        print('Digite o telefone.\n' + updatePerson.Telefone)
                        print(RED +"Digite um telefone valido"+ RESET)
                        continue
                    break
                
            if upi == 5:
                print('Digite o sexo. "h" para homem, "m" para mulher')
                while True:
                    updatePerson.Sexo = input()
                    if updatePerson.Sexo == 'h' or updatePerson.Sexo == 'm':
                        break
                    print('Digite o sexo. "h" para homem, "m" para mulher\n' + updatePerson.Sexo)
                    print(RED +"apenas 'h' e 'm' são aceitos"+ RESET)
                
            if upi == 6:
                print('Digite a profissão.')
                
                while True:
                    updatePerson.Profissao = input()
                    if not Validate(updatePerson.Profissao, "!@#$%*()-_=+[}{]~^'`,<.>;:/?\|*1234567890", True):
                        print('Digite a profissão.\n' + updatePerson.Profissao)
                        print(RED +"Digite uma profissão valida"+ RESET)
                        updatePerson.Profissao = ''
                        continue
                    break
                
            if upi == 7:
                print('Digite o email.')
                
                while True:
                    updatePerson.Email = input()
                    if not Validate(updatePerson.Email, "!#$%*()-=+[}{]~^'`,<>;:/?\|*", True):
                        print('Digite o email.\n' + updatePerson.Email)
                        print(RED +"Digite um email valido"+ RESET)
                        updatePerson.Email = ''
                        continue
                    break
                
            break
        
        lstCadastroLines[updateIndex + 1] = updatePerson.Nome + '\n'
        lstCadastroLines[updateIndex + 2] = updatePerson.Idade + '\n'
        lstCadastroLines[updateIndex + 3] = updatePerson.Endereco + '\n'
        lstCadastroLines[updateIndex + 4] = updatePerson.Telefone + '\n'
        lstCadastroLines[updateIndex + 5] = updatePerson.Sexo + '\n'
        lstCadastroLines[updateIndex + 6] = updatePerson.Profissao + '\n'
        lstCadastroLines[updateIndex + 7] = updatePerson.Email + '\n'
        stringUpdate = ''
        
        for i in range(lstCadastroLines.__len__()):
            stringUpdate = stringUpdate + lstCadastroLines[i]
        
        fd = open('./cadastros/bd-teste.txt', 'w')
        fd.write(stringUpdate)
        fd.close()
        os.system("clear")
        print('Alteração feita com sucesso.!')
        getchar()
        os.system("clear")
        
    if choice == 4: #delete
        fd = open('./cadastros/bd-teste.txt', 'r')
        lstCadastroLines = fd.readlines()
        fd.close()
        updateIndex = FindRegById(lstCadastroLines)
        updateIndex = updateIndex*ATRIBUTOSPESSOA
        updatePerson = Pessoa
        updatePerson.Id = lstCadastroLines[updateIndex]
        updatePerson.Nome = lstCadastroLines[updateIndex + 1].strip('\n')
        updatePerson.Idade = lstCadastroLines[updateIndex + 2].strip('\n')
        updatePerson.Endereco = lstCadastroLines[updateIndex + 3].strip('\n')
        updatePerson.Telefone = lstCadastroLines[updateIndex + 4].strip('\n')
        updatePerson.Sexo = lstCadastroLines[updateIndex + 5].strip('\n')
        updatePerson.Profissao = lstCadastroLines[updateIndex + 6].strip('\n')
        updatePerson.Email = lstCadastroLines[updateIndex + 7].strip('\n')
        
        while True:
            PrintDeletePessoa(updatePerson)
            deletar = getchar()
            if deletar == 'n':
                os.system("clear")
                break
            elif deletar == 's':
                lstCadastroLines[updateIndex + 0] = ''
                lstCadastroLines[updateIndex + 1] = ''
                lstCadastroLines[updateIndex + 2] = ''
                lstCadastroLines[updateIndex + 3] = ''
                lstCadastroLines[updateIndex + 4] = ''
                lstCadastroLines[updateIndex + 5] = ''
                lstCadastroLines[updateIndex + 6] = ''
                lstCadastroLines[updateIndex + 7] = ''
                stringUpdate = ''
                
                for i in range(lstCadastroLines.__len__()):
                    stringUpdate = stringUpdate + lstCadastroLines[i]
                
                fd = open('./cadastros/bd-teste.txt', 'w')
                fd.write(stringUpdate)
                fd.close()
                os.system("clear")
                print('Alteração feita com sucesso.!')
                getchar()
                os.system("clear")
            break
            