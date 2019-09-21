class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def insertLast(self, value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode

    def ViewList(self):
        if self.start == None:
            print("Empty list")
        else:
            temp = self.start
            while temp != None:
                print(temp.data)
                temp = temp.next

    def DeleteFirst(self):
        if self.start == None:
            print("linked list is empty")
        else:
            self.start = self.start.next

mylist=LinkedList()
for i in range(5):
    mylist.insertLast((input('enter the element')))
mylist.ViewList()
print()
mylist.DeleteFirst()
mylist.ViewList()