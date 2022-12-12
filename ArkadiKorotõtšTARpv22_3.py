#12/12/22
#1
from math import *
from random import *
from cmath import pi
from stringprep import c22_specials


print("Puu läbimõõdu arvutamine")
#Kirjuta programm, mis kusib kasutaja kaest puu umbermoodu ning teatab selle peale puu labimoodu
C=float(input("Anna umbermõõt: "))
d=round(C/pi, 2)
print(f"Puu labimõõt = {d}")

#2
#Arvutage Pythoni kasureal, kui pikk on ristkulikukujulise maatuki diagonaal, mille ootmed on Nm x Mm. N ja M kusi kasutajalt
N=float(input("Sisesta N: "))
M=float(input("Sisesta M: "))
d=round(sqrt(N**2+M**2), 2)
print(f"Ristkulikukujulise maatuki diagonaal on {d}")

#3
#Leidke järgnevast näiteprogrammist semantiline viga:
#aeg = float(input("Mitu tundi kulus soiduks? "))
#teepikkus = float(input("Mitu kilomeetrit soitsid? "))
#kiirus = aeg / teepikkus

#print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4
print("Aritmeetiline keskmine")
A1=int(input("Esimene arv: "))
A2=int(input("Teine arv: "))
A3=int(input("Kolmas arv: "))
A4=int(input("Neljas arv: "))
A5=int(input("Viies arv: "))
K=(A1+A2+A3+A4+A5)/5
print(f"Keskmine on {K}")

#5
print("Joonista samasugune konn")
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("  ^^ "'""'" ^^")

#6
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c 
print(f"Ümbermõõt on {P}")

#7
P=randint(2,6)
summa=(12.9*1.1)/P 
print(f"{P}-st sõprast, igaüks maksab {summa} ")

#8
print("kütusekulu arvutamine")
l=float(input("kütuse liitride kogus: "))
km=float(input("läbitud kilomeetrid: "))
kulu=(l/km)*100
print(f"kütusekulu {kulu}")

#9
print("Rulluisutajad")
M=int(input("Minutid:"))
M=M/60
tee=M*29.9
print(f"Jõuab {tee} km")

#10
print("Ajateisendus")
M=int(input("Sisesta aja minutites")) #1h=60min
H=M//60 #h
M=M%60 #MIN
print(f"{H}:{M}")
