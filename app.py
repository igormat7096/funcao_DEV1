# importação da biblioteca
import time 

# Funções = def 
# def representa uma função 
# em uma função usa verbos no infinitivo 

def dar_boas_vindas(usuario):
    print(f"Olá {usuario}. Seja bem vindo ao meu programa!")

#programa principal que vai chamar essa função 
print("Início do meu programa.")
time.sleep(2)
nome = input("Informe o nome do usúario: ")
dar_boas_vindas(nome)
time.sleep(2)
print("Programa encerrado.")