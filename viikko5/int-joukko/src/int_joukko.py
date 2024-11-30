KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti ei ole positiivinen kokonaisluku")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoko ei ole positiivinen kokonaisluku")
       
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.koko = 0

    def kuuluu(self, luku):
        for i in range(self.koko):
            if self.alkiot[i] == luku:
                return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.koko >= self.kapasiteetti:
                vanha_lista = self.alkiot
                self.alkiot = self._luo_lista(self.koko + self.kasvatuskoko)
                self.kopioi_lista(vanha_lista, self.alkiot)
            self.alkiot[self.koko] = luku
            self.koko += 1
            return True
        return False

    def poista(self, luku):
        poistettu = False
        for i in range(self.koko):
            if self.alkiot[i] == luku:
                poistettu = True
                self.koko -= 1
            elif poistettu:
                self.alkiot[i-1] = self.alkiot[i]
        return poistettu

    def kopioi_lista(self, lahto, maali):
        for i in range(len(lahto)):
            maali[i] = lahto[i]

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        lista = self._luo_lista(self.koko)
        for i in range(self.koko):
            lista[i] = self.alkiot[i]
        return lista

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for luku in a.to_int_list():
            x.lisaa(luku)
        for luku in b.to_int_list():
            x.lisaa(luku)
        return x

    @staticmethod
    def leikkaus(a, b):
        x = IntJoukko()
        for luku in a.to_int_list():
            if b.kuuluu(luku):
                x.lisaa(luku)
        return x

    @staticmethod
    def erotus(a, b):
        x = IntJoukko()
        for luku in a.to_int_list():
            if not b.kuuluu(luku):
                x.lisaa(luku)
        return x

    def __str__(self):
        if self.koko == 0:
            return "{}"
        elif self.koko == 1:
            return "{" + str(self.alkiot[0]) + "}"
        else:
            tuotos = "{"
            for luku in self.alkiot[:self.koko-1]:
                tuotos += str(luku) + ", "
            tuotos += str(self.alkiot[self.koko-1])
            tuotos += "}"
            return tuotos
