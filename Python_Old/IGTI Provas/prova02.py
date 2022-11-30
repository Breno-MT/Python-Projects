#sim eu não fiz pra primeira, eu esqueci
class Classe_1:
    def funcao_da_classe_1(self, string):
        dicionario = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        valor = 0
        for i in range(len(string)):
            if i > 0 and dicionario[string[i]] > dicionario[string[i - 1]]:
                valor += dicionario[string[i]] - 2 * dicionario[string[i - 1]]
            else:
                valor += dicionario[string[i]]
        return valor