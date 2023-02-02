'''
a="Hola Mundo" #primer hola mundo
print(a)
print(type("Hola"))
print(type(3))
print(type(3.55))
'''

'''Hola como estas
xddddddddddddddd
funciona lollll'''

'''
nombre,apellido = "David" , "Padilla"

print(nombre)
print(apellido)

exponente = 2**2 # ** se utiliza para exponentes
print(exponente)

DivisionEntero = 5//2 # // se utiliza para división entera
print(DivisionEntero)

Modulo = 70%3 # Modulo es el resto de una división
print(Modulo)

ejercicio1 = ((3+2)/(2*5))**2
print(ejercicio1)

calculo = pow(5,2) # pow es lo mismo que 5**2
print(calculo)

NumeroPayasos = 23
NumeroMunecas = 54
Payasos=112
Munecas=75

PesoTotal=NumeroPayasos*Payasos+NumeroMunecas*Munecas
print(PesoTotal)

texto="Ejemplo \"cadena\" de texto" 
print(texto)

texto2="Ejemplo \nsalto de linea"
print(texto2)

cadena1="Hola"
cadena2="David"
print(cadena1+" "+cadena2) # concatenación
print(cadena1*5)
print(cadena1,cadena2)

ejemplotexto="Este es un ejemplo de texto"
print(ejemplotexto[0:10])

print(ejemplotexto.lower())
print(ejemplotexto.upper())
print(ejemplotexto.capitalize())
print(ejemplotexto.title())
print(ejemplotexto.swapcase())

ejercicio1="Te quiero solo como amigo"
print(ejercicio1[0:2])
print(ejercicio1[-3: ])
EjercicioRecta="recta"
print(EjercicioRecta[::2])
EjercicioCadena="hola mundo!"
print(EjercicioCadena[::-1])
EjercicioReflejo="reflejo"
print(EjercicioReflejo+EjercicioReflejo[::-1])

ejercicio2="eparado"
remplazar=ejercicio2.replace("",",")
print("s"+remplazar)

nombre=input("Ingresa tu nombre:")
edad=input("Ingresa tu edad:")

print("Hola "+nombre+" tu edad es: "+edad)

'''
'''
a=int(input("Agrega el valor de a:"))
b=int(input("Agrega el valor de b:"))
c=int(input("Agrega el valor de c:"))

resolucionP=str(((0-1)*b+((b**2)-(4*a*c))**0.5)/2*a)
resolucionN=str(((0-1)*b-((b**2)-(4*a*c))**0.5)/2*a)

print("El resultado positivo: "+resolucionP)
print("El resultado negativo: "+resolucionN)

P1=int(input("Nota de 1 practica:"))
P2=int(input("Nota de 2 practica:"))
P3=int(input("Nota de 3 practica:"))
EP=int(input("Nota del examen parcial:"))
EF=int(input("Nota del examen final:"))

PP=(P1+P2+P3)/3
PROM=(PP+2*EP+3*EF)/6

resultado=str(PROM)

print("El promedio practica "+str(PP))
print("El promedio final es "+resultado)

nombre=input("Ingresa tu nombre:")
edad=int(input("Ingresa tu edad:"))

print("Hola {} tu edad es {}".format(nombre,edad))

vocal=str(input("Ingrese una vocal en minuscula:"))
letra=str(input("Ingrese una letra en mayúscula:"))

print("La vocal es: {} \nLa letra es: {}".format(vocal.lower(), letra.upper()))

nombre=input("Ingresa tu nombre:")
edad=input("Ingresa tu edad:")
sexo=input("Ingresa tu sexo:")

print("Te llamas: {} \nTu edad es: {} \nEres: {}".format(nombre,edad,sexo))

cadena="hola mundo"

print(cadena.startswith("H"))
print(cadena.endswith("o"))
print(cadena.isupper())
print(cadena.islower())

edad=17

if edad >18:
    print("Eres mayor de edad")
elif edad==18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")

nombre="Juan"
edad=20

if nombre=="David":
    if edad>=18:
        print("Eres David y mayor de edad")
    else:
        print("Eres David pero menor de edad")
elif edad>=18:
    print("No eres David pero mayor de edad")
else:
    print("No eres David y menor de edad")


respuesta=str(input("Ingresa una vocal:"))

if respuesta.lower()=="a":
    print("Es una vocal")
elif respuesta.lower()=="e":
    print("Es una vocal")
elif respuesta.lower()=="i":
    print("Es una vocal")
elif respuesta.lower()=="o":
    print("Es una vocal")
elif respuesta.lower()=="u":
    print("Es una vocal")
else:
    print("No es una vocal")

numero=int(input("Ingresa un numero entero:"))

if numero>=0:
    print(numero)
else:
    print(abs(numero))

primera_pl=str(input("Ingresa la primera palabra:"))
segunda_pl=str(input("Ingresa la segunda palabra:"))

lg_caracter_primera=len(primera_pl)#muestra la cantidad de caracteres
lg_caracter_segunda=len(segunda_pl)#muestra la cantidad de caracteres

primera_rima=primera_pl[-3: ]
segunda_rima=segunda_pl[-3: ]

primera_media_rima=primera_pl[-2: ]
segunda_media_rima=segunda_pl[-2: ]

if(lg_caracter_primera<3 or lg_caracter_segunda<3):
    print("No riman, porque tiene menos de 3 caracteres")
elif(primera_rima==segunda_rima):
    print("riman")
elif(primera_media_rima==segunda_media_rima):
    print("riman un poco")
else:
    print("no rima")


voto=str(input("Ingresa un candidato (A,B ó C):")).upper()

if(voto=="A" or voto=="B" or voto=="C"):
    if(voto=="A"):
        print("Usted ha votado por el partido rojo")
    elif(voto=="B"):
        print("Usted ha votado por el partido verde")
    elif(voto=="C"):
        print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")


lista=["python",100,4.5,True,"david"] #lista: se guardan varios datos parecido a un array

print(type(lista))
print(lista[2])
print(len(lista))
lista[0]="php"
print(lista)

#debanado de lista
print(lista[4])
print(lista[0:3])
print(lista[ :2])
print(lista[2: ])
print(lista[-2: ])

#metodo de lista
lista=[1,2,3,4,5,6,7,8]
lista.append(9)#agrega un valor a la lista siempre al final

print(lista)

lista.insert(2,2.5)#agrega un valor a la lista en posicion que se indica "2"
print(lista)

lista=[1,3,3,4,5,3,7,8]
print(lista.count(3))#cuenta la cantidad de veces que aparece "3"
print(lista.index(3))#busca la posicion del primer valor "3"

lista.sort()#ordena los valores en orden acendente
print(lista)

lista.reverse()#ordena los valores en orden decendente
print(lista)

lista=["php",2,"python",3,"javascript",4]
lista.pop()#elimina el ultimo valor de la lista
print(lista)

lista.remove("php")#elimina un valor expecifico "php"
print(lista)


primera_lista=[1,2,3]
segunda_lista=[4,5,6]

unir_lista=primera_lista+segunda_lista#se fucionan
print(unir_lista)
print(primera_lista,segunda_lista)#concatena

lista=[]

edad=int(input("Ingrese su edad:"))

lista.append(edad)
print(lista)


lista=[20, 50, "Curso", 'Python', 3.14]

primero=input("Ingrese el primer valor:")
segundo=input("Ingrese el segundo valor:")

lista[0]=primero
lista[1]=segundo

print(lista)

lista=[1,2,3,4,5,6,7,8,9,10]

lista[3]*=2
lista[6]*=2
lista[8]*=2

print(lista)


diccionario={"lenguaje":"php","usuario":"david"}

print(type(diccionario))
print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario["lenguaje"])

diccionario["lenguaje"]="python"
print(diccionario)

diccionario={"nombre":"david","apellido":"padilla","edad":4}
print(diccionario)

diccionario.pop("nombre")#elimina un key "nombre"
print(diccionario)

print(diccionario.get("edad"))#traer valor de el key "edad"

diccionario.clear()#borra todo el diccionario
print(diccionario)

diccionario.setdefault("estatura",1.7)#agrega contenido al diccionario
print(diccionario)

diccionario_2={"nombre":"arturo"}
diccionario.update(diccionario_2)#agrega un diccionario a otro
print(diccionario)

diccionario={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

valor=str(input("Ingrese un pais:").title())
if(diccionario.get(valor)!=None):
    print(diccionario.get(valor))
else:
    print("Ese pais no se encuentra")

diccionario={

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

valor=int(input("Ingrese un numero:"))

if(valor in diccionario): #si existe trae "True" si no "False"
    print(diccionario.get(valor))
else:
    print("El numero es incorrecto")

conjunto={1,2,3,4,5,6}#conjuntos
print(type(conjunto))

conjunto=set([(1,2,3,4,5,6)])#conjuntos
print(type(conjunto))

conjunto=set((1,2,3,4,5,6))#conjuntos
print(type(conjunto))

conjunto={1,1,2,3,4,5}#los elementos repetidos se muestran una vez
lista=[1,1,2,3,4,4]

print(conjunto)

#metodos
conjunto={1,2,3,4,5}
conjunto.add(6)#agrega un nuevo valor
print(conjunto)

conjunto.remove(1)#elimina un valor "1"
print(conjunto)

conjunto.update([7,8,9])
print(conjunto)

tupla=(1,2,3,4,5)#tuplas no se puede cambiar sus valores
tupla2=(6,7,8,9,10)

print(tupla)
print(type(tupla))
print(tupla[2])
print(tupla[0:3])
print(tupla+tupla2)

tupla=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre")

valor=int(input("Ingrese un numero:"))
print(tupla[valor-1])

n=1
while n<=10:
    print(n)
    n+=1

valor=int(input("Ingrese un numero:"))
string=str(valor)

i=0
while i<=10:
    print("{} x {} = {}".format(string,i,valor*i))
    i+=1

edad=int(input("Ingresa tu edad:"))

i=0
while i<edad:
    i+=1
    print(i)

lista=["David","Padilla","Morales"]
tupla=(1,2,3,4,5)

for i in lista:#for recorre lista
    print(i)

for j in tupla:
    print(j)

for i in range(1,5):
    print(i)

for j in range(1,10,2):
    print(j)

for i in range(1,10):
    print(i)
    if(i==5):
        break#luego de que se cumpla el if termina el bucle

for i in range(1,10):
    if(i==5):
        continue#luego de que se cumpla el if omite y continua
    print(i)

lista=[1,2,3,4,5,6,7,8,9,10]

print(lista)
primer_valor=int(input("Ingrese el primer numero:"))
segundo_valor=int(input("Ingrese el segundo numero:"))

if primer_valor==segundo_valor:
    print("Error los numeros son iguales")
elif primer_valor>segundo_valor:
    for i in range(segundo_valor,primer_valor):
        print(i)
else:
    for i in range(primer_valor,segundo_valor):
        print(i)

for i in range(primer_valor,segundo_valor+1):
    if i%2==0:
        continue
    print(i)

#funcion
lista=[1,2,3,4,5,6,7,8,9]
print(max(lista))
print(min(lista))

def saludo():
    print("Hola como estas")

saludo()

valor=int(input("Ingrese un numero:"))
def tabla(valor):
    for i in range(1,11):
        print("{} x {} = {}".format(valor,i,i*valor))

tabla(valor)

lista=[1,2,3,5,7,9,12,15,17]

def agrega():
    primer_n=int(input("Ingrese un numero:"))
    segundo_n=int(input("Ingrese un numero:"))
    tercero_n=int(input("Ingrese un numero:"))

    lista.append(primer_n)
    lista.append(segundo_n)
    lista.append(tercero_n)

    lista_par=[]
    lista_impar=[]

    for i in lista:
        if(i%2==0):
            lista_par.append(i)
        else:
            lista_impar.append(i)
        
        lista_par.sort()
        lista_impar.sort()

    print("Esta es la lista par: {}".format(lista_par))
    print("Esta es la lista impar: {}".format(lista_impar))

agrega()

def factorial():
    from math import factorial
    numero=int(input("Ingrese un numero:"))
    if numero>0:
        print(factorial(numero))
    else:
        print("El valor es incorrecto")

factorial()

import math
import random

print(math.pow(10,2))
print(math.sqrt(64))
print(math.isqrt(64))
print(math.sin(37))
print(math.cos(37))
print(math.tan(37))
print(math.factorial(5))

print(random.randint(1,100))


def ejercicio():
    primer_n=int(input("Ingrese el primer numero:"))
    segundo_n=int(input("Ingrese el segundo numero:"))

    if primer_n==segundo_n:
        return 0
    elif primer_n>segundo_n:
        return 1
    else:
        return -1

print(ejercicio())

def factura():
    valor=int(input("Ingrese el valor:"))
    iva=int(input("Ingrese el iva:"))
    if iva!=0:
        total=((valor*iva)/100)+valor
        return total
    else:
        total=valor*0.21+valor
        return total

print(factura())
'''

def valores():
    global num1
    global num2
    num1=60
    num2=30

    suma=num1+num2
    return suma

print(valores())
resta=num1-num2
print(resta)