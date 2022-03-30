import sys
import json
import clipboard

# Irá criar um arquivo chamado clipboard.json, aonde irá ficar os valores e chaves passados.
SAVED_DATA = "clipboard.json"

# Irá salvar os dados no arquivo, também pode escrever por cima de alguns que já existem caso o nome seja repetido.
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Irá ler os dados no arquivos para poder fazer o CTRL+V no teclado.
def load_data(filepath):

    try:

        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# Tem que ter 2 argumentos, sendo eles o nome do .py, e o argumento.
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    # Irá salvar o que está no clipboard atual, ou seja, vai pedir um nome pra Chave, e irá pegar o valor e guardar num dicionário.
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved successfully.")
    
    # Irá pegar o valor de alguma chave selecionada e irá colar automaticamente no CTRL+V
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print("Key doesn't exist.")

    # Irá mostrar uma lista do dicionario atual contendo os valores e chaves.
    elif command == "list":
        print(data)
    
    elif command == "remove":
        key = input('Enter a key: ')
        data.pop(key)
        save_data(SAVED_DATA, data)
        print(f"{key} has been removed.")

    else:
        print('Unknown commmand.')
else:
    print('Please pass exactly one command.')

