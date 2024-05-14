# Faça um programa que subtraia 2 horas da hora atual utilizando timedelta.

from datetime import datetime, timedelta

# Obtém a hora atual
hora_atual = datetime.now()

# Subtrai 2 horas da hora atual
hora_subtraida = hora_atual - timedelta(hours=2)

# Mostra a hora subtraída
print("Hora atual:", hora_atual)
print("Hora há 2 horas:", hora_subtraida)
