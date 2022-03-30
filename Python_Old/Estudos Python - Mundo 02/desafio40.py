nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <5.0:
    print('Sua média é {:.1f}! Portanto, você está \033[31mREPROVADO\033[m! Estude mais da próxima vez!'.format(media))
elif 5.0 < media <6.9:
    print('Sua média é {:.1f}! Portanto, você está de \033[33mRECUPERAÇÃO\033[m! Se esforçe e estude mais!'.format(media))
else:
    print('Sua média é {:.1f}! Portanto, você está \033[32mAPROVADO\033[m! \033[36mParabéns campeão\033[m!'.format(media))
