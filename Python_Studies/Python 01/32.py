# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("Rachel",19),
            ("Monica",18),
            ("Phoebe",17),
            ("Joey",16),
            ("Chandler",21),
            ("Ross",20)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)



viados_menos_Breno = [("Breno", 19),
            ("Farias", 19), 
            ("Isaac", 19), 
            ("Carbono", 18), 
            ("Dornelles", 20)]

idade = lambda data: data[1] == 19

amigos_maior_19 = list(filter(idade, viados_menos_Breno))

for i in amigos_maior_19:
    print(i)
