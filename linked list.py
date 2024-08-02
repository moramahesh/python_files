# class Node:
#     def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None
      
# class SLinkedList:
#    def __init__(self):
#       self.headval = None

#    def listprint(self):
#       current_node = self.headval
#       while current_node is not None:
#          print (current_node.dataval)
#          current_node = current_node.nextval
# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# # Link first Node to second node
# list.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3

# list.listprint()
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,val):
        if self.head == None:
            self.head=Node(val)
        else:
            cur =self.head
            while(cur.next):
                cur=cur.next
            cur.next=Node(val)
    def display(self):
        if self.head ==None:
            return 
        else:
            cur=self.head
            while(cur):
                print(cur.data,end ="->")
                cur=cur.next
    def insertatindex(self,pos,val):
        newnode=Node(val)
        cur = self.head
        pos=pos-1
        while(pos>0):
            cur = cur.next
            pos-=1
        newnode.next=cur.next
        cur.next=newnode
    def removeatindex(self,pos,val):
        newnode=Node(val)
        cur = self.head
        pos=pos-1
        while(pos>0):
            cur = cur.next
            pos-=1
        cur.next=cur.next.next
    
l=Linkedlist()
l.append(7)
l.append(8)
l.append(2)
l.append(9)
l.display()
print()
l.insertatindex(2,16)
l.display()
