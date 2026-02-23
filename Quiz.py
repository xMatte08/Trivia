import csv
import random

file_path = 'CSVdomande.csv'
Listadomande = []

with open(file_path, 'r', newline ="",encoding='utf-8') as file:
    reader = csv.reader(file)
    for elemento in reader:
        Listadomande.append(elemento)
'''
for elemento in Listadomande :
    print(f"({elemento[0]}, {elemento[5]})")  
'''
nDomande = 0
for elemento in Listadomande:
    nDomande += 1
nDomande += -1

domandeUscite = []
presente = True
numero = 0
for i in range(10):
    presente = True
    while presente:  
        presente = False
        numero = random.randint(1,nDomande)
        if numero in domandeUscite:
            presente = True
        
    domandeUscite.append(numero)
    print(Listadomande[numero][0])
giuste = 0
giusto = True
if giusto == True: 
    giuste += 1
print(giuste)