import rekins
from input import rekins

def datuIevade():
    klients = input("Ievadi vārdu: ")
    veltijums = input("Ievadi veltījumu: ")
    izmers = input("Ievadi izmēru (platums,garums,augstums): ")
    materials = input("Ievadi materiāla cenu EUR/m2: ")
    print('\n')
    dati = rekins(klients,veltijums,izmers,materials)
    dati.saglabat()
    dati.izdrukat()

    print('\nRekina Aprekins!\n')



while True:
    print('1) Datu Ievade | 2) Iziet')
    Izvele = input('Izvelaties: ')

    if Izvele == '1':
        datuIevade()
    elif Izvele == '2':
        break
    else:
        print('Ievadi darbibas numuru')
        continue