n = int(input('Entre com um número não negativo: '))
fatorial = 1
for i in range(1,n+1):
    fatorial = fatorial * i
print(str(n)+ '! = ', fatorial)
