class Animal:

    def scoate_sunet(self):
        print("Animalul scoate sunete generale")

class Pisica(Animal):

    def scoate_sunet(self):
        print("Pisica scoate sunete specifice")

class Catel(Animal):

    def scoate_sunet(self):
        super().scoate_sunet()
        print("Pe langa sunetele generale, catelul scoate si sunete specifice")


c1 = Catel()
c1.scoate_sunet()