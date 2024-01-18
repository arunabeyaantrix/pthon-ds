class HashTable:
  def __init__ (self, size = 7):
    self.data_map = [None] * size

  def __hash(self, key):
    my_hash = 0
    for letter in key:
      my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
    return my_hash
  
  def print_table(self):
    for i, value in enumerate(self.data_map):
      print(i, ':', value)
    
  def set_item(self, key, value):
    index = self.__hash(key)
    if self.data_map[index] == None:
      self.data_map[index] = []
    self.data_map[index].append([key, value])

my_table = HashTable()

my_table.set_item('BOLT', 4)
my_table.set_item('Iteme', 5)
my_table.set_item('iteme2', 6)

my_table.print_table()

