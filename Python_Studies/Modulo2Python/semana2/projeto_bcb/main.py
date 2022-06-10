from bcb import currency
import matplotlib.pyplot as plt

# ipca = currency.get(('IPCA', 433), last=12)
moedas = currency.get(['USD', 'EUR'], start='2000-01-01', end='2021-06-09', side='ask')

# plt.plot(moedas)
moedas.plot(figsize=(12, 6));
plt.show()
