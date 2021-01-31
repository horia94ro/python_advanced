class Pisica:

    _nr_mangaieri = 0

    @staticmethod
    def despre_pisica():
        print('Pisica vrea sa fie alintata!')
        print(Pisica._nr_mangaieri) #dacă vrem să apelăm aici zona de memorie _nr_mangeieri o facem direct din numele clasei
        #acest lucru s-ar întampla la fel și dacă metoda despre_pisica ar fi definită în cadrul unui alt fișier, întrucât
        #ea nu cunoaște informații despre clasa Pisica în sine

    @classmethod
    def alinta_pisica(cls, nr_alinturi):
        print('Alintam pisica...')
        for i in range(nr_alinturi):
            cls._rasfata_pisica()
        #spre deosebire de metoda despre_pisica(), în această metodă ne putem folosi de parametrul cls, care va face
        #referire directă la clasa în care metoda este definită

    @classmethod
    def _rasfata_pisica(cls):
        cls._nr_mangaieri += 1

p1 = Pisica()
p1.despre_pisica()
p1.alinta_pisica(5)
Pisica.despre_pisica()
Pisica.alinta_pisica(3)
