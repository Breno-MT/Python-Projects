from time import sleep

def process_data(data):
    print('Iniciando o processamento de algum dado...')
    modified_data = data + ' o dado foi modificado.'
    sleep(3)
    print('Processamento do dado terminado.')
    return modified_data

def read_data_from_web():
    print('Lendo dados da web')
    data = 'Dados da web lidos'
    return data

def write_data_to_database(data):
    print('Armazenamento dados em um database')
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
