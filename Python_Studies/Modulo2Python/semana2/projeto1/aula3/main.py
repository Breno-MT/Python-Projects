from collections import namedtuple

# tupla = (10,)

# print(type(tupla))

Estados = namedtuple('Estado', ['sigla', 'nome', 'regiao'])

estado_rj = Estados("RJ", "Rio de Janeiro", "Sudoeste")
estado_sp = Estados("SP", "São Paulo", "Sudeste")
estado_sc = Estados("SC", "Santa Catarina", "Sul")

print(estado_rj)
print(estado_sp)
print(estado_sc)