############################# **kwargs = parametro que ira pacotar todos argumentos em um dicionario
############################# util para que a função aceite varios argumentos de keyword argumentos ( ja foi visto no file "08.py")

#def hello(**names):
    #print("Hello " + kwargs["first"] + " " + kwargs["last"])
    #print("Hello",end=" ")
    #for key,value in names.items():
        #print(value, end=" ")

#hello(title="Sr.",first="Breno", middle="Martins",last="Teixeira")

############################# str.format() = metodo opcional que da para o usuario mais controle quando mostra display output ( imagem que aparece pos código )

#animal = "cow"
#item = "moon"

#print("The {} jumped over the {} !" .format(animal, item))
#print("The {animal} jumped over the {item} !" .format(animal="cow", item="moon"))
#print("The {0} jumped over the {1} !" .format(animal, item))
#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "Breno"

#print("Hello, my name is {}!".format(name))
#print("Hello, my name is {:10}!".format(name))
#print("Hello, my name is {:<10}!".format(name))
#print("Hello, my name is {:>10}!".format(name))
#print("Hello, my name is {:^10}!".format(name))

num = 1000
#print("The number pi is {:.2f}".format(num))
print("The number pi is {:,}".format(num))
print("The number pi is {:b}".format(num))
print("The number pi is {:o}".format(num))
print("The number pi is {:X}".format(num))
print("The number pi is {:e}".format(num))