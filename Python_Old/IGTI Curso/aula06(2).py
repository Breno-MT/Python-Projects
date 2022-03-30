nome_do_arquivo = 'lyrics3.txt'
letra = open(nome_do_arquivo)
lista_linhas = []
linha = letra.readline().rstrip()
while linha != 'FIM':
    lista_linhas.append(linha)
    linha = letra.readline().rstrip()
for i in lista_linhas:
    print(i)
