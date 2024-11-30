class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = arvo

    def miinus(self, operandi):
        self._edellinen_arvo = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edellinen_arvo = self._arvo
        self._arvo = self._arvo + operandi
    
    def nollaa(self):
        self._edellinen_arvo = self._arvo
        self._arvo = 0

    def kumoa(self):
        self._arvo = self._edellinen_arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
    
    def suorita(self):
        self._vanha_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(self._syote())

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
    
    def suorita(self):
        self._vanha_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(self._syote())

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        self._vanha_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        self._sovelluslogiikka.kumoa()
    