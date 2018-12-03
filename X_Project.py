"""
Questo è il main code del progetto richiesto per il midterm pratico di ingegneria degli algoritmi
"""


from linkedListDictionary import LinkedListDictionary
from avlTree import AVLTree

class Partizione:
    def __init__(self, min, max, b):
        assert max>min, "Massimo minore di minimo. Inserire i valori correttamente"
        assert b>6, "B deve essere maggiore di 6!"
        assert ((max-min)/b)%2==0, "B deve essere divisore di max - min"
        self.max = max
        self.min = min
        self.b = b
        self.d = int((max - min)/b) #da fare il modulo
        self.list = []
        for i in range(self.d + 2):
            self.list.append(LinkedListDictionary())


    def insert1(self, key, value):
        if(key >= self.max):
            if (self.checkType(self.list[self.d+1])):
                self.list[self.d+1].insert(key, value)
                print("elemtento inserito")
                if(self.list[self.d+1].theList.len_list() == 6):
                    pass
            else:
                self.list[self.d + 1].insert(key, value)
                print("elemtento inserito")
        elif(key < self.min):
            if (self.checkType(self.list[self.d])):
                self.list[self.d].insert(key, value)
                print("elemtento inserito")
                if (self.list[self.d + 1].theList.len_list() == 6):
                    pass
            else:
                self.list[self.d + 1].insert(key, value)
                print("elemtento inserito")
        else:
            for i in range(self.d):
                if(key >= self.min + (i*self.b) and key < self.min + ((i + 1) * self.b)):
                    if(self.checkType(self.list[i])):
                        self.list[i].insert(key, value)
                        print("elemtento inserito")
                        if (self.list[self.d + 1].theList.len_list() == 6):
                            pass
                        break
                    else:
                        self.list[self.d + 1].insert(key, value)
                        print("elemtento inserito")

    def serch(self, key):
        pass


    def delete(self, key):
        pass

    def checkType(self, l):
        if (type(l) is LinkedListDictionary):
            return True
        else:
            return False


if __name__ == "__main__":
    dic = Partizione(1, 17, 8)

    dic.insert1(3, "prova 1")
    dic.insert1(1, "prova 2")

    dic.insert1(19, "prova 2")
    dic.insert1(20, "prova 2")
    dic.insert1(21, "prova 2")
    dic.insert1(22, "prova 2")
    dic.insert1(23, "prova 2")
    dic.insert1(24, "prova 2")

