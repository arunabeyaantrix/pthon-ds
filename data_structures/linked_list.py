class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = temp

        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length-= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.pop()

my_ll.print_list()