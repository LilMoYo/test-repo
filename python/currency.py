# Write code below 💖

pesos = int(input('What do you have left in Colombian pesos? '))
soles = int(input('What do you have left in Peruvian soles? '))
reais = int(input('What do you have left in Brazilian reais? '))

p1 = float(pesos * 0.00024)
s1 = float(soles * 0.27)
r1 = float(reais * 0.17)

total_usd = p1 + s1 + r1

print(total_usd)
print('Your total is: '+ str(total_usd) + ' USD')