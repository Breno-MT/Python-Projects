from tkinter import *
from time import *

def atualizacao():
    tempo_str = strftime("%H:%M:%S " +"h") # Str Horas: Minutos: Segundos
    tempo_label.config(text=tempo_str) # Configurando para colocar o texto do tempo

    dia_str = strftime("%A") # Str Dia da semana completa.
    dia_label.config(text=dia_str)

    data_str = strftime("%d %B, %Y") # %d Dia(01 até 31), %B Nome do Mes, %Y Ano Ex: 2001
    data_label.config(text=data_str)

    window.after(1000, atualizacao) # Irá atualizar a cada 1 sec, ou a cada 1000 milisegundos


window = Tk()

# **** Tempo Horas: Minutos: Segundos****
tempo_label = Label(window, font=("M PLUS 1", 25), fg="black") # Label do Tempo
tempo_label.pack()

# **** Dia da semana ****
dia_label = Label(window, font=("Shippori Antique", 15)) # Label do dia
dia_label.pack()

# **** Data com nome do Mes e o Ano ****
data_label = Label(window, font=("Consolas", 15)) # Label da Data
data_label.pack()

atualizacao() # Irá chamar a função atualização. ( Auto explicativo. )

window.mainloop()