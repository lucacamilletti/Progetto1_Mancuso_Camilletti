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


    def insert_main(self, key, value):
        pos = self.find_list(key)
        if (self.checkType(self.list[pos])):
            self.list[pos].insert(key, value)
            print("elemtento inserito")
            if (self.list[pos].theList.len_list() == 6):
                self.changeAVL(self.list[pos], pos)
        else:
            self.list[pos].insert(key, value)
            print("elemtento inserito")

    def search_main(self, key):               #da abbellire
        pos = self.find_list(key)
        if (self.checkType(self.list[pos])):
            print(self.list[pos].search(key))
        else:
            print(self.list[pos].search(key))


    def delete_main(self, key):
        pos = self.find_list(key)
        if (self.checkType(self.list[pos])):
            self.list[pos].delete(key)
            print("elemtento eliminato")
        else:
            self.list[pos].delete(key)
            print("elemtento eliminato")
            if (self.list[pos].theList.len_list() == 6):
                pass

    def checkType(self, l):
        if (type(l) is LinkedListDictionary):
            return True
        else:
            return False


    def changeAVL(self, list, i):
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

    def changeInList(self, list, i):
        linkedList = LinkedListDictionary()
        self.l = list


    def find_list(self, key):
        if (key >= self.max):
            return self.d+1
        elif (key < self.min):
            return self.d
        else:
            for i in range(self.d):
                if(key >= self.min + (i*self.b) and key < self.min + ((i + 1) * self.b)):
                    return i

    def print(self):
        for i in range(self.d+2):
            print(self.list[i])


if __name__ == "__main__":
    dic = Partizione(1, 17, 8)

    dic.insert_main(19, "prova 2")
    dic.insert_main(20, "prova 2")
    dic.insert_main(21, "prova 2")
    dic.insert_main(22, "prova 2")
    dic.insert_main(23, "prova 2")
    dic.insert_main(24, "prova 2")
    dic.insert_main(25, "prova 2")
    dic.insert_main(26, "prova 2")
    dic.insert_main(27, "prova 2")
    dic.insert_main(28, "prova 2")

    dic.search_main(26)


    if type(dic.list[3]) is AVLTree:
        print("funziona")

    else:
        print("non funziona")

    dic.print()