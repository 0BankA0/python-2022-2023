class Rekins():
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers.split(",")
        self.materials = float(materials)

        
        
        
        self.aprekins()

    def izdrukat(self):
        print("Klients:",self.klients)
        print("Veltījums:",self.veltijums)
        print("Izmērs:", self.izmers)
        print("Materiāls:",self.materials)
        print("apmaksas suma", self.aprekins())

    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (len(self.veltijums)) * 1.2 + int(self.izmers[0])/100 * int(self.izmers[1])/100 * int(self.izmers[2])/100/ 3 * int(self.materials)
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100 
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        return rekina_summa 

klients = input("ievadi vardu: ")
veltijums= input("Ievadi veltījumu: ")
izmers= input("ievadi izmerus (platums,garums,augstums): ")
materieals= input("ievadi materiala cenu EUR/m2: ")



pirmais = Rekins(klients,veltijums,izmers,materieals)
pirmais.izdrukat()