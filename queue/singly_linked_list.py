class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, value):
      # wrap value in node
      new_node = Node(value)
      # if linked list is empty
      if self.head is None:
        self.head = new_node
        self.tail = self.head
      # if linked list is not empty
      else:
        self.tail.next_node = new_node
        self.tail = new_node

    def remove_from_head(self):
      # if linked list is empty
      if self.head is None:
        return None
      else:
        return_val = self.head.value
        # if there is only one node in linked list
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next_node
        return return_val

    def count_nodes(self):
      count = 0
      
      # if linked list is empty
      if self.head is None:
        return count
      else:
        cur_node = self.head
        while cur_node != None:
          count += 1
          cur_node = cur_node.next_node
      
      return count



    
                