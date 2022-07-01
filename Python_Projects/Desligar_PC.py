import os

# O único jeito de não executar, é só dando CTRL+C, mais pra frente faço um menu :D

sec = int(input("Digite em segundos o tempo para desligar o PC: "))

os.system(f"shutdown /s /t {sec}")
