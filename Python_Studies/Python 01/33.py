# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#           perfoms function at first two elements and repeats process until 1 value remains
# reduce(function, iterable)

import functools

#letters = ["H", "E", "L", "L", "O"] # mesma coisa que ali em baixo, porém ele concatenar
#word = functools.reduce(lambda x,y: x+y,letters)
#print(word)

factorial = [5,4,3,2,1] # 5*4=20, 20*3=60, 60*2=120, 120*1=120
result = functools.reduce(lambda x,y: x*y, factorial)
print(result)