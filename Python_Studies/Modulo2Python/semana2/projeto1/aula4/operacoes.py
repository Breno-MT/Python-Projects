set_a = {6,9,12,24,21}
set_b = {9,53,12,21,30}


# Diferença
# (pertence A e não pertencem a B)

print("Diferença")
print(set_a ^ set_b) # igual a de baixo
print(set_a.difference(set_b)) # igual a de cima

print("---"*9)

# Diferença Simétrica
# (itens que pertencem aos dois conjuntos e que não estão interseção)

print("Diferença Simétrica")
print(set_a ^ set_b)
print(set_a.symmetric_difference(set_b))

print("---" * 9)

# União 
# (união dos dois conjuntos)
print("União")
print(set_a | set_b)
print(set_a.union(set_b))

print("---"*9)

# Interseção 
# (pertencem ao conjunto A e B)
print("Interseção")
print(set_a & set_b)
print(set_a.intersection(set_b))

print("---"*9)