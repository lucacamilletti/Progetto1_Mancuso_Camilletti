"""
Questo è il main code del progetto richiesto per il midterm pratico di ingegneria degli algoritmi
"""

from Dictionary import Dictionary
from linkedListDictionary import LinkedListDictionary
from avlTree import AVLTree
from binarySearchTree import BinarySearchTree

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
                if(self.list[self.d+1].theList.len_list() >= 6):
                    self.changeAVL(self.list[self.d+1], self.d+1)
            else:
                self.list[self.d + 1].insert(key, value)
                print("elemtento inserito")
        elif(key < self.min):
            if (self.checkType(self.list[self.d])):
                self.list[self.d].insert(key, value)
                print("elemtento inserito")
                if (self.list[self.d].theList.len_list() == 6):
                    self.changeAVL(self.list[self.d], self.d)
            else:
                self.list[self.d].insert(key, value)
                print("elemtento inserito")
        else:
            for i in range(self.d):
                if(key >= self.min + (i*self.b) and key < self.min + ((i + 1) * self.b)):
                    if(self.checkType(self.list[i])):
                        self.list[i].insert(key, value)
                        print("elemtento inserito")
                        if (self.list[i].theList.len_list() == 6):
                            self.changeAVL(self.list[i], i)
                        break
                    else:
                        self.list[i].insert(key, value)
                        print("elemtento inserito")
                        break

    def serch(self, key):               #da abbellire
        if (key >= self.max):
            if (self.checkType(self.list[self.d+1])):
                print(self.list[self.d+1].search(key))
            else:
                print(self.list[self.d+1].search(key))
        elif (key < self.min):
            if (self.checkType(self.list[self.d])):
                print(self.list[self.d].search(key))
            else:
                print(self.list[self.d].search(key))
        else:
            for i in range(self.d):
                if(key >= self.min + (i*self.b) and key < self.min + ((i + 1) * self.b)):
                    if(self.checkType(self.list[i])):
                        print(self.list[i].search(key))
                        break
                else:
                    print(self.list[i].search(key))

    def delete(self, key):
        pass

    def checkType(self, l):
        if (type(l) is LinkedListDictionary):
            return True
        else:
            return False


    def changeAVL(self, list, i = 0):
        avlTree = AVLTree()
        self.l = list
        current = self.l.theList.first
        while current != None:
            key = current.elem[0]
            value = current.elem[1]
            avlTree.insert(key, value)
            current = current.next
        del self.list[i]                #possibile usare entrambi i metodi
        self.list.insert(i, avlTree)
        #self.list[i] = avlTree


if __name__ == "__main__":
    dic = Partizione(1, 17, 8)

    dic.insert1(19, "prova 2")
    dic.insert1(20, "prova 2")
    dic.insert1(21, "prova 2")
    dic.insert1(22, "prova 2")
    dic.insert1(23, "prova 2")
    dic.insert1(24, "prova 2")
    dic.insert1(25, "prova 2")
    dic.insert1(26, "prova 2")

    dic.serch(26)


    if type(dic.list[3]) is AVLTree:
        print("funziona")

    else:
        print("non funziona")