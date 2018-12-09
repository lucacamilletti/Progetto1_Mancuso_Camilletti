"""
Questo è il main code del progetto richiesto per il midterm pratico di ingegneria degli algoritmi
"""


from LinkedList.linkedListDictionary import LinkedListDictionary
from Tree.avlTree import AVLTree


class Partizione:

    def __init__(self, min, max, b):
        assert max>min, "Massimo minore di minimo. Inserire i valori correttamente"
        assert b>6, "B deve essere maggiore di 6!"
        assert (max-min)%b==0, "B deve essere divisore di max - min"
        self.max = max
        self.min = min
        self.b = b
        self.d = int(abs((max - min)/b))
        self.list = []
        for i in range(self.d + 2):
            self.list.append(LinkedListDictionary())

    def insert_main(self, key, value):
        pos = self.find_list(key)
        if (self.checkType(self.list[pos])):
            self.list[pos].insert(key, value)
            if (self.list[pos].theList.len_list() == 6):
                avl = self.changeInAVL(self.list[pos])
                self.list[pos] = avl
        else:
            self.list[pos].insert(key, value)

    def search_main(self, key):
        pos = self.find_list(key)
        if self.checkType(self.list[pos]):
            return self.list[pos].search(key)
        else:
            return self.list[pos].search(key)

    def delete_main(self, key):
        pos = self.find_list(key)
        if (self.checkType(self.list[pos])):
            self.list[pos].delete(key)
        else:
            self.list[pos].delete(key)
            if (self.list[pos].size() == 6):
                linked = self.changeInList(self.list[pos])
                self.list[pos] = linked

    def checkType(self, l):
        if (type(l) is LinkedListDictionary):
            return True
        else:
            return False

    def changeInAVL(self, list):
        avlTree = AVLTree()
        self.l = list
        current = self.l.theList.first
        while current != None:
            key = current.elem[0]
            value = current.elem[1]
            avlTree.insert(key, value)
            current = current.next

        return avlTree

    def changeInList(self, lis):
        linkedList = LinkedListDictionary()
        for i in range(5):
            s = lis.tree.root
            linkedList.insert(s.info[0], s.info[1])
            lis.balDelete(s)

        return linkedList

    def find_list(self, key):
        if (key >= self.max):
            return self.d + 1
        elif (key < self.min):
            return self.d
        else:
            return int((key-self.min)/self.b)

    def print(self):
        for i in range(self.d+2):
            print(self.list[i])



if __name__ == "__main__":
    dic = Partizione(100, 1100, 10)

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

    dic.delete_main(28)
    dic.delete_main(27)
    dic.delete_main(26)
    dic.delete_main(25)
    dic.delete_main(24)



    if type(dic.list[3]) is AVLTree:
        print("funziona")

    else:
        print("non funziona")

    dic.print()

# del self.list[pos]  # possibile usare entrambi i metodi
# self.list.insert(pos, linked)
