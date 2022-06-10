from bcb import sgs
import matplotlib.pyplot as plt

ipca = sgs.get(('IPCA', 433), last=12)

plt.plot(ipca)
plt.show()
