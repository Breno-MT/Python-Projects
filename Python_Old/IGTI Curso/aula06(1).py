nome_do_arquivo = 'lyrics3.txt'
letra = open(nome_do_arquivo)
numerolinhas = 0
linha=letra.readline().rstrip()
while linha != 'FIM':
    numerolinhas = numerolinhas + 1
    linha = letra.readline().rstrip()
print(nome_do_arquivo + ' possui ' + str(numerolinhas) + ' linhas.')
