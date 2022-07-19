class Node:
    def __init__(self,d):
        self.next = None
        self.data=d
        
    def display(self):
        print(self.data, end='  ')
class LinkedList:
    def __init__(self):
        self.head = None
        self.size =  0
        
    def Add_head(self,data):
        if self.head == None:
            self.head = data
            self.size = self.size + 1
        else:
            data.next = self.head
            self.head = data
            self.size = self.size + 1
            
    def Add_tail(self,data):
        if self.head == None:
            self.head = data
            self.size = self.size + 1 
            return
        else:
            Temp = self.head
            while Temp.next != None:
                Temp = Temp.next
            Temp.next = data
            self.size = self.size + 1
    
    def third_last_element(self):
        return self.get_3rd_last_element(self.head,3)
    
    def get_3rd_last_element(self,head, k):
        NODE = 0
        temp = head
        while temp:
            temp = temp.next
            NODE = NODE + 1
        if NODE >= k:
            temp = head
            for i in range(NODE - k):
                temp = temp.next
        return temp.data
    
    def reverse(self):
        Prev_Node = None
        temp = self.head
        while(temp is not None):
            next = temp.next
            temp.next = Prev_Node
            Prev_Node = temp
            temp = next
        self.head = Prev_Node
        
    def Display_Values(self):
        temp = self.head
        while(temp != None):
            temp.display()
            temp = temp.next
    
l=LinkedList()
l.Add_head(Node(1))
l.Add_head(Node(5))
l.Add_head(Node(2))
l.Add_head(Node(3))
l.Add_tail(Node(4))
l.Display_Values()
print()
print("3rd last element of linked list is: ", l.third_last_element())
l.reverse()
l.Display_Values()
l.Add_tail(Node(7))
print()
l.Display_Values()
