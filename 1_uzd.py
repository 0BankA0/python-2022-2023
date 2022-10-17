class Ballite():
    def __init__(self,dekoracijas, ciemini, ediens, vel_davanas):
        self.dekoracijas = dekoracijas
        self.ciemini = ciemini
        self.ediens = ediens
        self.velDavanas = vel_davanas

    def pirkumi(self):
        print('nopirc dekoracijas:')
        for a in self.dekoracijas:
            print(a)
        print('Nopirc eienus:')
        for a in self.ediens:
            print(a)

    def Davanas(self):
        print('davanu sarkats:')
        for a in self.velDavanas:
            print(a)

dzD = Ballite(["Baloni","Virtene","Salvetes"],["Anna","Pēteris","Zeltīte","Valters"],["Kartupeļi","Gurķi","Burkāni","Kūka","Sula"],["Grāmata","Krājkase","Termokrūze"])
print(dzD.ediens)
dzD.pirkumi()
dzD.Davanas()