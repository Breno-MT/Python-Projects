############################# dictionary = mudavel, desorganizado
############################# coleções de chaves unicas de valores pares, pra acessar um valor rapido

capitals = {"USA":"Washington DC", "India":"New Dehli",
"China":"Beijing", "Russia":"Moscow"}

#print(capitals["Germany"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Las Vegas"})
#capitals.pop("China")
#capitals.clear()

#for key,value in capitals.items():
    #print(key, value)

############################# index operator = da acesso para sequencia do elemento (str, list, tuples)

name = "breno martins"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)



# list_sorted = sorted(lista_de_anotacao, key=lambda value:value["Nivel"], reverse=True)


#     if list_sorted == []:
#         print("[!] A lista está vazia.")
    
#     else:
#         for x in list_sorted:
#             print(len(f"[>] {x}"))