
import random
import math

x1 = 0
x2 = 0

def generateNewState(x1, x2):
    x1 = random.uniform(-10,10)
    x2 = random.uniform(-10,10)
    return(x1,x2)

(x1, x2) = generateNewState(x1, x2)

def E(x1, x2):
    hasil = -((math.sin(x1)*math.cos(x2))+((4/5)*math.exp(1-math.sqrt(math.pow(x1,2)+math.pow(x2,2)))))
    return hasil

E0 = E(x1, x2)
bestSoFar = x1, x2
EBest = E0
T = 1000 #100,10,1
deltaT = 0.1

while T>0:
    x1b, x2b = generateNewState(x1, x2)
    Eb = E(x1b, x2b)
    deltaE = Eb-E0
    print("x1 baru     : ", x1b)
    print("x2 baru     : ", x2b)
    print("E baru      : ", Eb)
    print("delta E     : ", deltaE)
    if deltaE<=0:
        (x1, x2) = (x1b, x2b)
        E0 = Eb
        if Eb<EBest:
            bestSoFar = (x1, x2)
            EBest = E0
            
    else:
        p = math.exp(-deltaE/T)
        r = random.uniform(0, 1)
        if r<p:
            (x1, x2) = (x1b, x2b)
            E0 = Eb

    print(" ")        
    T = T-deltaT


print("Hasil Akhir")
print("Best So Far : ", bestSoFar)
print("E Best Awal : ", E0)
print("E Best Akhir: ", EBest)