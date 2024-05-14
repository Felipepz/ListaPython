import random

def leitura_sensor():
    for _ in range(10):
        yield random.randint(0, 100)

sensor = leitura_sensor()

for leitura in sensor:
    print("Leitura do sensor:", leitura)
