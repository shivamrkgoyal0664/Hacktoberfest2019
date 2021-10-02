class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def add_begin(self,data):

        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        #print(new_node.data)

    def add_between(self,data,prev_node):
        if prev_node == None:
            print ("empty")

        else:
            #temp=self.head
            new_node=node(data)
            #while(temp.data != prev_node):
            
            new_node.next=temp.next
            temp.next=new_node
    
    def add_end(self,data):
        temp=self.head
        new_node=node(data)
        while (temp.next != None):
            
            new_node.next=None
            temp.next=new_node
            print(new_node.data)
    def print_LL(self):
        n=self.head
        #print(n)
        while(n != None):
            print(n.data)
            n=n.next
ll=linkedlist()
ll.add_begin(11)
ll.print_LL()
#ll.add_end(33)
ll.add_between(10,33)
ll.print_LL()