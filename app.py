import random
import string

senha = ""
numero = ["0","1","2","3","4","5","6","7","8","9"]
letra = list(string.ascii_lowercase)
letraupper = list(string.ascii_uppercase)
letras = letra + letraupper
tamanhoSenha = range(0,8)
senhageral = letras + numero

while True:
    print("\nBem vindo ao gerador de senha\n")
    print("1 - Senha somente com números!\n2 - Senha somente com letras!\n3 - Senha com todos os caracteres\n4 - Para sair")
    opcao = input()

    if(opcao == "1"):
        for x in tamanhoSenha:
                var = random.choice(numero)
                senha += var
        print(senha)
        senha = ""
        

    elif(opcao == "2"):
        for x in tamanhoSenha:
            var = random.choice(letras)
            senha += var
        print(senha)
        senha = ""
        
    
    elif(opcao == "3"):
        for x in tamanhoSenha:
            var = random.choice(senhageral)  
            senha += var
        print(senha)
        senha = ""
                

    elif(opcao == "4"):
        break