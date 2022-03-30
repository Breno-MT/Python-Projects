import random

# Fazer um gerador de password

# 1. Uma variavel que contenha as letras de a-z, A-Z, números (0-9), símbolos (!@#$%&*-_)

letras = "abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&^*-_"

while True:
    password_tamanho = int(input("Qual o tamanho da sua senha?: "))
    password_quantidade = int(input("Quantas senhas você deseja ter?: "))

    for i in range(0, password_quantidade):
        password = ""
        for h in range(0, password_tamanho):
            password_letras = random.choice(letras)
            password = password + password_letras
        print(f"Aqui está sua senha!: {password}")