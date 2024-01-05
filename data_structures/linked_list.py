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
    def get(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.head
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self,index,value):
        if index < 0 or index >= self.length:
            return False
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        else:
            return False
    
    def insert(self,index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        before = self.get(index - 1)
        after = before.next
        new_node.next = after
        before.next = new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        before = self.get(index - 1)
        after = temp.next

        before.next = after
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        if self.length = 0 or self.length == 1:
            return True
        before = None
        temp = self.head
        after = temp.next
        self.head = self.tail
        self.tail = temp

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True



my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.pop()

print(my_ll.get(4).value)

my_ll.print_list()