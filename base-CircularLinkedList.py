# ===========================================
 # By: Luis Felipe Rueda García 
 # Nury Farelo - Estructuras Datos
 # Name: Lista Circular Doblemente Enlazada 
 # ===========================================

#Clase Nodo
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#Clase Lista Doblemente Enlazada
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insertHead(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.next=newNode
            newNode.prev=newNode
            self.head=newNode
            self.tail=newNode
            #self.head.next=self.head
            #self.head.prev=self.head
            
            return True
        else:
            newNode.prev = self.head.prev
            newNode.next = self.head

            self.head.prev = newNode
            self.tail.next = newNode
            
            self.head = newNode
            return True



    def IsEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def insertTail(self, data):
        if self.tail is None:
            self.insertHead(data)
        else:
            newNode = Node(data)
            newNode.prev = self.head.prev
            newNode.next = self.head

            self.head.prev = newNode
            self.tail.next = newNode
            
            self.tail = newNode
            return True

