class No:
    def __init__(self, charge: object = None, ant: 'No' = None, prox: 'No' = None):
        self.charge = charge
        self.ant    = ant
        self.prox   = prox

    def __str__(self):
        return str(self.charge)

class ArrayListCircle:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if(self.head is None):
            print("List is none")
            return

        current: 'No' = self.head
        print(current)

        while current is not self.tail:
            print(current.prox)
            current = current.prox
    
    def insertInTheBeginning(self, value: object):
        new: 'No' = No(value)
        
        if(self.head is None):
            self.head = self.tail = new
        
        else:
            new.prox        = self.head
            self.head       = new 
            new.prox.ant    = new
            self.head.ant   = self.tail
            self.tail.prox  = self.head

    def insertInTheEnd(self, value):
        new: 'No' = No(value)

        if(self.head is None):
            self.head = self.tail = new
        
        else:
            new.ant         = self.tail
            new.ant.prox    = new
            self.tail       = new 
            self.tail.prox  = self.head
            self.head.ant   = self.tail

    def removeInTheBeginning(self):
        if(self.head is None):
            print ("List is none")
            return

        if(self.head == self.tail):
            self.head = self.tail = None
        
        else:
            self.head       = self.head.prox
            self.head.ant   = self.tail
            self.tail.prox  = self.head
    
    def removeInTheEnd(self):
        if(self.head is None):
            print("List is none")
            return

        if(self.head == self.tail):
            self.head = self.tail = None
        
        else:
            self.tail = self.tail.ant
            self.tail.prox = self.head
            self.head.ant = self.tail

    def cout(self):
        con = 0
        current = self.head
        
        if(current is not None):
            con += 1
            current = current.prox

            while( current is not self.head):
                con += 1
                current = current.prox
        
        return con

