################################# type casting = converte o tipo de data de um valor para outro.
#x = 1 #int
#y = 2.0 #float
#z = "3" #str = string não da para utilizar o MATH, ou seja, não tem como somar ou subtrair de str, apenas de FLOAT e INT.

#x = float(x)
#y = float(y)
#z = float(z)
# -->print("X is "+str(x)) PODE SER SUBSTITUIDO POR .FORMAT() // EX: print('X is {}' .format(x))
#print(x*3,y*3,z*3)

################################# user input = aceitar input de usuarios
#name = input("What's your name?: ")
#age = int(input("What's your age?: "))
#height = float(input("How tall are you?: "))

#print("Hello {} ! Your age is {} years old, and you're {}cm tall!".format(name, age, height))

################################# math functions
#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi)) # valor absoluto de um numero
#print(pow(pi,2)) # a variante X elevada ao numero desejado.
#print(math.sqrt(pi)) # raiz quadrada
#print(max(x,y,z)) # maior numero entre as variantes
#print(min(x,y,z)) # o menor numero entre as variantes

################################# slicing = cria um substring extraindo elementos de outra string. // indexing[] ou slice() // [start:stop:step]
##### INDEXING
#name = "Breno Martins"

#first_name = name[:5] ## ou first_name = name[0:5]
#last_name = name[6:] ## ou last_name = name[6:13]
#idk_name = name[0:13:2] ## ou idk_name = name[::2]
#reversed_name = name[::-1]
#print(reversed_name)
##### SLICE
#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)

#website1[slice]
#print(website1[slice])
#print(website2[slice])