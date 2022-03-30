from xml.dom import minidom  #importa o modulo para leitura de arquivos xml
nome_do_arquivo_xml = 'arquivo_xml.xml'  #nome do arquivo a ser importado
documento_xml = minidom.parse(nome_do_arquivo_xml)
print(documento_xml)

#nós presentes no documento
nos = documento_xml.documentElement
print(nos.tagName)

#extraindo elementos de um arquivo xml
#cada elemento em um arquivo xml tem um nome
lista_de_compras = documento_xml.getElementsByTagName('item')
print(type(lista_de_compras))
lista_de_compras[0]

#acessando os atributos de um arquivo
for item in lista_de_compras:
    print(item.attributes['name'].value)

#acessando os elementos de um arquivos
for item in lista_de_compras:
    print(item.firstChild.data)
    