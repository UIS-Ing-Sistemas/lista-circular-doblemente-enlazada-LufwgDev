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



    def isEmpty(self):
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

    
    def deleteElement(self,x):
        #if (self.isValueOnList(x)):
        currentTemporalNode = None
        pastTemporalNode = None
        escape = False
        if self.isEmpty():
            return False
        else:
            currentTemporalNode=self.head
            pastTemporalNode=currentTemporalNode.prev

            if currentTemporalNode.data == x:
                self.head=currentTemporalNode.next
            if pastTemporalNode.data == x:
                self.tail=pastTemporalNode.prev

            while escape !=True:

                if currentTemporalNode.data == x:
                    
                    pastTemporalNode.next=currentTemporalNode.next
                    futureTemporalNode=currentTemporalNode.next
                    futureTemporalNode.prev=pastTemporalNode
                    return True
                else:
                    if currentTemporalNode.next!=self.head:
                        pastTemporalNode=currentTemporalNode
                        currentTemporalNode = currentTemporalNode.next
                    else:
                        escape = True
        return False

    def printElements(self,order):
        if self.isEmpty():
            return False
        else:
            if order:
                
                temporalNode = self.head
                head = self.head
                i=0
                while(temporalNode!=head or i==0):
                    print(temporalNode.data)
                    temporalNode=temporalNode.next
                    i=i+1
            else:
                tail = self.tail
                temporalNode= self.tail
                i=0
                while(temporalNode!=tail or i==0):
                    print(temporalNode.data)
                    temporalNode=temporalNode.prev
                    i=i+1
                
    def lenght(self):
        count = 0
        if self.isEmpty():
            return count
        else:
            temporalNode = self.head
            head = self.head
            while(temporalNode!=head or count==0):
                count=count+1
                temporalNode=temporalNode.next
        return count


#Tests
mylist = CircularLinkedList()
for i in range(10):
    mylist.insertTail(3*i)

#mylist.printElements()

for i in range(1,7):
    mylist.insertHead(7*i)

mylist.printElements(True)
print(f"hay {mylist.lenght()} elementos")
mylist.deleteElement(18)
mylist.deleteElement(42)
print(f"hay {mylist.lenght()} elementos")
mylist.printElements(True)
mylist.printElements(False)

