from rekins import Rekins

#WHILE cikls!!!!!
print("ŠEIT JĀBŪT PROGRAMMAS APRAKSTAM!")
klients = input("Ievadi vārdu: ")
veltijums = input("Ievadi veltījumu: ")
izmers = input("Ievadi izmēru (platums,garums,augstums): ")
materials = input("Ievadi materiāla cenu EUR/m2: ")

pirmais = Rekins(klients,veltijums,izmers,materials)
pirmais.saglabat()
pirmais.izdrukat()