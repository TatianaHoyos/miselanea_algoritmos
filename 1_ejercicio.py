'''
Se debe realizar un muestreo con 50 personas para determinar el promedio de peso de los 
niños, jóvenes, adultos y viejos que existen en su zona habitacional.   
Se determinan las categorías así:

CATEGORIA			EDAD
Niños				0 - 12
Jóvenes				13 - 29
Adultos				30 - 59
Viejos				60 en adelante
'''
peso_n=0
contador_n=0
peso_j=0
contador_j=0
peso_a=0
contador_a=0
peso_v=0
contador_v=0
for n_personas in range(0,5,1):
    print("persona # ", n_personas)
    edad=int(input("digite su edad: "))
    peso=float(input("digite su peso: "))
    zona=input("pertenece a esta zona: ")
    if zona.lower()=="si":
        if edad>=0 and edad <=12:
            contador_n=contador_n+1
            peso_n=peso_n+peso
        elif edad>12 and edad<=29:
            contador_j=contador_j+1
            peso_j=peso_j+peso
        elif edad>29 and edad<=59:
            contador_a=contador_a+1
            peso_a=peso_a+peso
            
        elif edad>59 :
            contador_v=contador_v+1
            peso_v=peso_v+peso

if contador_n==0:
  print("no hubo niños")
else:
    promedio_n=peso_n/contador_n
    print("el promedio de el peso de niños es de: ", promedio_n," hubo un total de: ", contador_n)
if contador_j==0:
  print("no hubo jovenes")
else:
    promedio_j=peso_j/contador_j
    print("el promedio de el peso de joven es de: ", promedio_j ," hubo un total de: ", contador_j)
if contador_a==0:
  print("no hubo adultos")
else:
    promedio_a=peso_a/contador_a
    print("el promedio de el peso de adulto es de: ", promedio_a," hubo un total de: ", contador_a)
if contador_v==0:
    print("no hubo viejos")
else:
    promedio_v=peso_v/contador_v
    print("el promedio de el peso de viejos es de: ", promedio_v," hubo un total de: ", contador_v)
    





