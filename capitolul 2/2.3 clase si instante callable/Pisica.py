class Pisica(object):

    def __init__(self, viteza):
        self.viteza = viteza

    def __call__(self, *args, **kwargs):
        print("Pisica alearga cu viteza: {}".format(self.viteza))


p1 = Pisica(10)
p1() #se va apela comportamentul definit în metoda __call__()
print(callable(p1)) #va returna True întrucât am suprascris metoda __call__()