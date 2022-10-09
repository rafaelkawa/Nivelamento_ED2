# # Questão 1
sequencia = []
sequencia.append(1)
sequencia.append(7)
sequencia.append(2)
sequencia.append(9)
print (sequencia)

i=4
while i < 100:
    sequencia.append(sequencia[i-4] + sequencia[i-3])
    i+=1

print (sequencia)


# #Questão 2
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, n):
        if self.head:
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(n)
        else:
            self.head = Node(n)

    def printList(self):
        pointer = self.head
        while(pointer != None):   
            print( pointer.data, end = " ")
            pointer = pointer.next

    def sort(self):
        if self.head == None:
            return
        pointer = self.head
        while (pointer != None):
            i = pointer.next
            while(i != None):
                if(pointer.data > i.data):
                    n = i.data
                    i.data = pointer.data
                    pointer.data = n
                i = i.next
            pointer = pointer.next

# # TESTE
# # lista = LinkedList()
# # lista.add(1)
# # lista.add(5)
# # lista.add(4)
# # lista.add(3)
# # lista.add(2)
# # lista.add(6)
# # lista.add(7)
# # lista.printList()
# # lista.sort()
# # lista.printList()

        
# #Questao 3
# # Sim. 
# # 1) Percorrer a string a partir do primeiro caracter e ir guardando em uma pilha, até achar um espaço (fim da palavra)
# # 2) Achando um espaço, desempilhar a pilha colocando os caracteres numa nova string
# # 3) Adicionar espaço na string nova 
# # 4) Repetir o processo até o fim da string inicial 


#Questão 4
class PriorityQueue:
    def __init__(self):
        self.first = None

    def isEmpty(self):
        return self.first == None

    def insert(self, n):
        newNode = Node(n)
        if self.isEmpty():
            self.first = self.last = Node(n)
        else:
            if self.first.data >= n:
                newNode.next = self.first
                self.first = newNode 
            else:
                current = self.first
                while current.next:
                    if n >= current.next.data:
                        current = current.next
                    else:
                        newNode.next = current.next
                        current.next = newNode
                        return
                self.last.next = newNode
                self.last = newNode
                return

    def pop(self):
        if not self.isEmpty():
            self.first = self.first.next
        print("Fila está vazia")
        return 

    def printQueue(self):
        pointer = self.first
        while(pointer != None):   
            print( pointer.data, end = " ")
            pointer = pointer.next


#Teste
# FilaTeste = PriorityQueue()
# FilaTeste.insert(90)
# FilaTeste.insert(68)
# FilaTeste.insert(11)
# FilaTeste.insert(70)
# FilaTeste.insert(1)
# FilaTeste.insert(12)
# FilaTeste.insert(70)
# FilaTeste.insert(200)
# FilaTeste.printQueue()


#Questão 5
class Stack:
    def __init__(self):
        self.top = None


    def push(self, n):
        node = Node(n)
        node.next = self.top
        self.top = node


    def pop(self):
        if self.top != None:
            node = self.top
            self.top = self.top.next
            return node.data
        else: 
            print("Erro: pilha vazia")
            return

    def peek(self):
        return self.top.data

    def printStack(self):
        pointer = self.top
        while(pointer != None):   
            print( pointer.data, end = " ")
            pointer = pointer.next

    def menu(self, action):
        match action:
            case 'Proxima Pagina':
                self.push('pagina')
            case 'Voltar Pagina':
                self.pop('pagina')
                
#Questao 6       
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, n):
        if self.head:
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(n)
        else:
            self.head = Node(n)

    def printList(self):
        pointer = self.head
        while(pointer != None):   
            print( pointer.data, end = " ")
            pointer = pointer.next

    def printMid(self):
        pointer = doublepointer = self.head

        if self.head is None:
            print("Lista Vazia")
        while (doublepointer != None and pointer != None):
            pointer = pointer.next
            doublepointer = doublepointer.next.next
        print (pointer.data)

#TESTE
# lista = LinkedList()
# lista.add(1)
# lista.add(2)
# lista.add(3)
# lista.add(4)
# lista.add(5)
# lista.add(6)
# lista.add(7)
# lista.add(8)
# lista.add(9)
# lista.add(10)
# lista.printList()
# lista.printMid()

#Questao 7
#Fila
class Player:
    def __init__(self):
        self.fila = []
    
    def adiciona(self, musica):
        self.queue.append(musica)
   
    def toca(self):
        if not len(self.fila == 0):
            nova = self.fila[0]
            del self.fila[0]
            return nova

#Questao 8
#35, 33, 42, 10, 14, 19, 27, 44, 26, 31
class Remedios:
    def __init__(self):
        self.lotes = []

    def insert(self, n):
        self.lotes.append(n)
    
    def sizeLotes(self):
        return len(self.lotes)

    def ordena(self):
        for i in range(self.sizeLotes()):
            for j in range(0, self.sizeLotes() - i - 1):
                if self.lotes[j] > self.lotes[j+1]:
                    temp = self.lotes[j]
                    self.lotes[j] = self.lotes[j+1]
                    self.lotes[j+1] = temp

#Primeiro adicionamos os numeros correspondentes aos lotes, em qualquer ordem, em uma lista.
#Depois chamamos o metodo "ordena" que percorre a nossa lista e a ordena utilizando um algoritmo bubble sort,
#que consiste em passar para o final da lista o maior elemento, dentre comparações entre pares dentro da lista.

#Teste:
remessa = Remedios()
remessa.insert(35)
remessa.insert(33)
remessa.insert(42)
remessa.insert(10)
remessa.insert(14)
remessa.insert(19)
remessa.insert(27)
remessa.insert(44)
remessa.insert(26)
remessa.insert(31)

print(remessa.lotes)
remessa.ordena()
print(remessa.lotes)
