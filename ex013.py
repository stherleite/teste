prod = float(input('Digite seu salário:R$'))
aut15 = prod + (prod * 15/100)
aut20 = prod + (prod * 20/100)
aut25 = prod + (prod * 25/100)
print('\n-->Antes, seu salário era R${:.2f},com um aumento de 15%, seu salário é de R${:.2f} ; \ncom um aumento de 20%, é de R${:.2f} ; \ne com um aumento de 25%, seu salário ficará R${:.2f}'.format(prod, aut15, aut20, aut25))