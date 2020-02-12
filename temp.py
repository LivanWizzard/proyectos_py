# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList
#print(aList)
cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
cList == dList
print(cList)


# =============================================================================
# listA = [1, 4, 3, 0]
# listB = ['x', 'z', 't', 'q']
# listA.extend([4, 1, 6, 3, 4])
# print(listA.pop(4))
# =============================================================================

# =============================================================================
# x = [1, 2, [3, 'John', 4], 'Hi'] 
# print(3 in x)
# =============================================================================



#uso de tuplas semana3
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    for i in range(0,len(aTup),2):
        newTup = newTup + (aTup[i],)

    return newTup
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
"""


#problem set2 ex3
#calculo de cuota con biseccion
"""
balance = 245059; annualInterestRate = 0.21
interes_mensual = annualInterestRate/12
#print("interes mensual: ",interes_mensual)
lower = round(balance/12,2)
#print("lower: ",lower)
upper = round((balance*(1+interes_mensual)**12)/12,2)
#print("upper: ",upper)
cuota_minima = (lower+upper)/2
def calculo_interes_anual(balance,cuota_minima,interes_mensual):
    for i in range(12):
        balance = balance - cuota_minima
        #print("balance pagando la cuota minima de: ",cuota_minima," quedando: ",balance)
        balance = balance + (interes_mensual*balance)
        #print("balance mas interes: ",balance)
    return balance
#print(calculo_interes_anual(balance,29157.09,interes_mensual))
while True:
    awa=calculo_interes_anual(balance,cuota_minima,interes_mensual)
    #print(awa)
    if awa <=0.01 and awa >= 0.001:
        print("Lowest Payment: " + str(round(cuota_minima,2)))
        break
    elif awa > 0.01:
        #print(cuota_minima)
        lower = cuota_minima
        #print("cuota muy baja")
    elif awa < 0.0009:
        #print(cuota_minima)
        upper = cuota_minima
        #print("cuota muy alta")
    cuota_minima = (lower+upper)/2
"""




#problem set2 ex2
"""
balance = 3926
annualInterestRate = 0.2
cuota_minima = 10
    
def cuota_min_anual(balance,annualInterestRate,cuota_minima):
    balance_original = balance
    interes_mensual = annualInterestRate/12
    #print("interes mensual: ",interes_mensual)
    for i in range(12):
        balance = balance - cuota_minima
        #print("balance pagando la cuota minima de: ",cuota_minima," quedando: ",balance)
        balance = balance + (interes_mensual*balance)
        #print("balance mas interes: ",balance)
    if balance < 0:
        return "Lowest Payment: " + str(cuota_minima)
    else:
        #print(balance)
        balance = balance_original
        cuota_minima += 10
        #print(cuota_minima)
        return cuota_min_anual(balance,annualInterestRate,cuota_minima)

print(cuota_min_anual(balance,annualInterestRate,10))
"""   


#examen1 ex 4
"""
def fibonacci(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        nuevo = 0
        prim = 1
        seg = 1
        for i in range(1,a):
            nuevo = prim +seg
            prim =seg
            seg = nuevo
    return nuevo
print(fibonacci(3))
"""


#examen1 ex3
"""
import re

def validate(username):
    inicio = re.search("^[a-zA-Z]",username)
    caracteres =  re.search("[a-zA-Z]+[0-9]*",username)
    #print("coincide letra en inicio: ",inicio)
    fin = re.search("_$",username)
    barras = username.count("_")
    #print("coincide guin bajo al final: ",fin)
    espacios =  re.search("\s",username)
    if len(username) < 4:
        return False
    else:
        if inicio and fin==None and espacios == None and barras <= 1 and caracteres:
            return True
        else:
            return False

print(validate("Mike_Standish")) #Valid username
print(validate("Mike988Standish9")) #Invalid username


"""





#examen1 ex2
"""
def john_mary(str):
    cadena = str.casefold()
    johns = cadena.count("john")
    marys = cadena.count("mary")
    if johns == marys:
        return True
    else:
        return False

print(john_mary('John&Mary'))
"""


#examen1 ex1
"""
import math
def areas(r, a):
    """
"""
    :param r: (float) The radius of the circle.
    :param a: (float) The angle of the segment.
    :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
"""
"""
    area_circulo_completo = math.pi*r**2
    segment_area = (r**2/2)*(a*math.pi/180 - math.sin(a*(math.pi/180)))
    area2 = area_circulo_completo-segment_area
    return segment_area, area2

print(areas(10, 90));
"""

#problem set 2 ex 1
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(0,12):
    #print("balance sin pagar: ",balance)
    #print("pago minimo mensual: ",balance * monthlyPaymentRate)
    pago_minimo_mensual = balance*monthlyPaymentRate
    #print("restante: ",balance-pago_minimo_mensual)
    balance = round(balance-pago_minimo_mensual,2)
    #print("interes: ",(annualInterestRate/12.0*balance))
    interes = round((annualInterestRate/12.0*balance),2)
    balance += interes
print(round(balance,2))

"""




"""
#!/bin/python3
# Complete the minimumBribes function below.
def minimumBribes(Q):
    moves = 0  # numero de movimientos
    Q = [P-1 for P in Q] #Este compa nos regresa las posiciones como deberian ir
    #ej: [2,1,5,3,4] => [1,0,4,2,3] = Q
    #print(Q)
    for i,P in enumerate(Q):
        # P es la posicion original
        # P en caso de ejemplo = 
        # P en iteracion 0 = 2 pero su posicion es 1
        # P en iteracion 1= 1 pero su posicion es 0
        # P en iteracion 2= 5 pero su posicion es 4
        # Etcetera xd || Entonces sabemos que son los valores uno por uno en Q
        # i es el numero pues original 1, 2, 3, 4, 5 segun se itere este rollo
        # (P-i) 
        # Más bien la diferencia de P(Pos original) y la actual i()
        # Entonces en la condicion vemos si:
        # P = 1 menos i = 0 [En la primer iteracion] = X
        # X es o bien si va ahí y no incrementa los moviemientos,
        # Si lo movieron para atras (-1) y tampoco es movimiento sumado
        # Si es un resultado 1 o 2, es que se movio adelante una o dos veces
        # O bien, significa que salto demás
        #ej: 2 1 5 3 4
        # 2 dio un paso enfrente = 1
        # 1 dio uno atras        =-1
        # 5 dio dos enfrente     = 2
        # 3 dio uno atras        =-1
        # 4 dio uno atras        =-1
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
           # print("j=",j)
           # print("Q[j]=",Q[j])
            if Q[j] > P:
                moves += 1
    print(moves)
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
"""




#functions 9
#encontrar una letra en un string ordenado alfabeticamente de forma recursiva
#y con el metodo de biseccion
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    if char > aStr[len(aStr)-1]:
        return False
    ans = len(aStr)//2
    if char == aStr[ans]:
        return True
    elif char < aStr[ans]:
        return isIn(char,aStr[:ans])
    else:
        return isIn(char,aStr[ans:])
print(isIn("f","abcdef"))
"""



#functions 8
#maximo comun divisor entre a y b de forma recursiva
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
"""     



#functions 7
#maximo comun divisor entre a y b de forma iterativa
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 1 or b == 1:
        return 1
    else:
        awa = min(a,b)
        if a % awa == 0 and b % awa == 0:
            return awa
        else:
            for i in range(awa):
                awa -=1
                if a % awa == 0 and b % awa == 0:
                    return awa
"""



#functions 6
#exponente de forma recursiva
#falta estudiar mas este metodo
"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        if exp == 1:
            return base
        else:
            return base * recurPower(base,exp-1)
"""



#functions 5
#exponente de forma iterativa
"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    awa = base
    for i in range(exp-1):
        base *= awa

    return base
"""

#functions 4
#regresando True or False de un num inpar
"""
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x % 2 != 0
"""

#functions 3
#usando la funcion de square en funcion de cuarta potencia
"""
def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(x) * square(x)
"""

#functions 2
"""
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x**2+b*x+c
"""



#functions 1
"""
def square(x):
    '''
    x: int or float.
    '''
    #print(x**2)
    return x**2

print(square(2))
"""



#guesses
#biseccion
"""
low = 0
high = 100
ans = (low + high)/2
print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number " , ans, "?")
    res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if res == "h":
        high = ans
    elif res == "l":
        low = ans
    elif res == "c":
        print("Game over. Your secret number was: ",ans)
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = (high + low)//2
"""


#subestrings
"""
s = "azcbobobegghakl"
tamano = len(s)
res = ""
temp = ""
mayor=""
actual = ""
letra=0
for letters in s:
    if tamano <= 1:
        res = letters
        print("Longest substring in alphabetical order is: "+res)
    else:
        temp = letters
        if res =="":
            res = temp
            if res == "z":
                mayor = res
        else:
            if res[len(res)-1] <= temp:
                res+=temp
                actual = res
            else:
                if len(actual)>len(mayor):
                    mayor=res
                res = temp
if len(mayor)>=len(res):
    print("Longest substring in alphabetical order is: "+mayor)
else:
    print("Longest substring in alphabetical order is: "+res)
"""


"""
tamaño = len(s)
actual = ""
comparar = 0
temp = ""
mayor = ""
res = ""
awa = True
for letters in s:
    comparar = len(res)-1
    if tamaño <=1:
        res = letters
        print("Longest substring in alphabetical order is: "+res)
        awa = False
    else:
        print("actual es: "+res+" y se va a comparar con: "+letters)
        if res[comparar] <= letters:
            res += letters
            awa = True
            if len(res) == len(s):
                print("Longest substring in alphabetical order is: "+res)
                awa = False
        else:
            temp = res
            res = letters
if len(res) > len(temp) and awa:
    print("Longest substring in alphabetical order is: "+res)
elif awa:
    print("Longest substring in alphabetical order is: "+temp)
"""