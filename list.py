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


mylist=LinkedList()
for i in range(int(input())):
    mylist.insertLast((input('enter the element')))
mylist.ViewList()
