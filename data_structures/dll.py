class Node:
  def __init__(self,value):
    self.value = value
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self,value):
    new_node = Node(value)
    if self.length == 0:
      self.head == new_node
      self.tail == new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1

  def pop(self):
    if self.length == 0:
      return None
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = temp.prev
      temp.prev = None
      self.tail.next = None
    self.length -= 1
    return temp
  
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True

  # pop_first
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = temp.next
      temp.next = None
      self.head.prev = None
    self.length -= 1
    return temp
  # get
  def get(self,index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp
  # set
  def set(self,index,value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    else: 
      return False
  # insert
  def insert(self,index,value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    temp = self.get(index - 1)
    after = temp.next
    new_node.next = after
    new_node.prev = temp
    temp.next = new_node
    after.prev = new_node
    self.length += 1
    return True

  def remove(self,index):
    temp = self.get(index)
    if index == 0:
      return self.pop_first()
    if index == self.length -1:
      return self.pop()
    if temp:
      before = temp.prev
      after = temp.next
      temp.prev = None
      temp.next = None
      before.next = after
      after.prev = before
      self.length -= 1
      return temp
    else:
      return None
  
  def print_list(self):
    temp = self.head
    while temp:
        print(temp.value)
        temp = temp.next
    return

my_ll = DoublyLinkedList(1)
# my_ll.append(2)
# my_ll.append(3)
# my_ll.append(4)
# my_ll.append(5)
my_ll.pop()
my_ll.pop()

my_ll.print_list()
  