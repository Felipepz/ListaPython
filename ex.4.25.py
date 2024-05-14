# Faça um programa que adicione 30 dias à data atual utilizando timedelta.


from datetime import datetime, timedelta

data_atual = datetime.now()

data_futura = data_atual + timedelta(days=30)

# Mostra a data futura
print("Data atual:", data_atual)
print("Data daqui a 30 dias:", data_futura)
