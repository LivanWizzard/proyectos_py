# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:34:41 2020

@author: Livan Martinez
"""
#awawawawawa


#problema de la cola de feria pendiente por terminar
"""        
def organizar(queue,contador,vueltas):
    vueltas -= 1
    for i in range(len(queue)-1):
        n1 = int(queue[i])
        n2 = int(queue[i+1])
        print("x:",n1,"y:",n2)
        if abs(n1-n2) <= 2:
            if n2 < n1:
                aux1 = n1
                queue[i]=n2
                queue[i+1]=aux1
                print(queue)
                contador +=1
    if queue == queue_original:
        return contador
    elif queue != queue_original and vueltas > 0:
        return organizar(queue,contador,vueltas)
    elif queue != queue_original and vueltas <= 0:
        return "Too chaotic"

t = int(input())
for t_itr in range(t):
    contador = 0
    aux1 = 0
    vueltas = 3
    queue_original = []
    
    n = int(input())

    q = list(map(int, input().rstrip().split()))
    for i in range(1,len(q)+1):
        queue_original.append(i)
    
    print(organizar(q,contador,vueltas))
"""


#2 5 1 3 4 caotic
#2 1 5 3 4 posible

#problema 4
"""
start = int(input("start: "))
end = int(input("end: "))
array =  []
for i in range(start,end):
    if i % 3 == 0:
        if i % 5 == 0:
            array.append("FizzBuzz")
        else:
            array.append("fizz")
    elif i % 5 == 0:
        array.append("buzz")
    else:
        array.append(i)
print(array)
"""

#problema 3
"""
n1 = input(list)
n2 = input(list)
count = 0
for i in range(1,len(n1),2):
    if int(n1[i]) - int(n2[i]) <= 2 or int(n2[i]) - int(n1[i]) <=2:
        if int(n1[i]) - int(n2[i]) <= 1 or int(n2[i]) - int(n1[i]) <=1:
            count += 1
print(count)
"""


#problema 2
"""
array = input(list)
awa = 0
res = []
for i in range(1,len(array),2):
    count = array.count(array[i])
    if int(array[i]) == int(count) and awa != array[i]:
        awa = array[i]
        res.append(awa)
        print(awa)

"""

#ejercicio uno
"""
import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9])
print(np.amax(array) - np.amin(array))
"""



#uso de las funciones map y lamnda
"""
cube = lambda x: x**3 #com lamda declaras una funcion para ciertos parametros(x)

def fibonacci(n):
    if n == 0:
        array = []
    elif n == 1:
        array = [0]
    elif n == 2:
        array = [0,1]
    else:
        array = [0,1]
        nuevo = 0
        prim = 0
        seg = 1
        for i in range(2,n):
            nuevo = prim + seg
            prim = seg
            seg = nuevo
            array.append(nuevo)
    return array
n = int(input())
print(list(map(cube, fibonacci(n)))) #con map haces uso de 2 funciones(la operacion, datos)
"""

#area del circulo
"""
from math import pi
r = float(input("radio: "))
print(str(pi*r**2))
"""

#arrays
"""
datos = input("ingrese datos: ")
tamaño = 0
lista = []
for char in datos:
    if char != ",":
        lista.append(char)
        tamaño += 1
print(lista)
"""

#pares e impares entre rangos
"""
n = int(input("ingrese un numero: "))
if n % 2 !=0:
    print("Weird")
elif (n%2==0) and (n >= 2 and n<=5):
    print("Not Weird")
elif (n%2==0) and (n >= 6 and n <= 20):
    print("Weird")
elif (n%2==0) and n >= 21:
    print("Not Weird")
"""

#suma, resta, multi
"""
a = int(input("num1: "))
b = int(input("num2: "))
print(a+b)
print(a-b)
print(a*b)
"""

#divisiones
"""
a = int(input("num1: "))
b = int(input("num2: "))
print(a//b)
print(a/b)
"""

#potencias
"""
n = int(input("nume: "))
for a in range(n):
    print(a**2)
"""

#años biciestos
"""
def is_leap(year):
    leap =  False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 :
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
year = int(input("year: "))
print(is_leap(year))
"""

#suecion con print
"""
n = int(input("numero: "))
for i in range(n):
    print(i+1,end='')
"""