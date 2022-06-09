import random

#random.seed(2) # inicia a semente para manter um padrão, dependendo da forma pode não haver mudanças


print(random.randint(0,20))

random_list = random.sample(range(10,30), 5)
print("Random List")
print(random_list)

print('Aleatórios pares:')
print(random.randrange(0,50,2))

items = [1,2,3,4,5,6,7,8,9,10]
print('Embaralhar items')
random.shuffle(items)
print(items)


print("Escolhendo um item da lista de forma aleatória")
print(random.choice(items))