class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
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

    def add_to_end(self, value):
        new_node = Node(value)
        # if the list is empty
        if not self.head:
            self.head = new_node
        # if the list ins't empty
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.next_node
            current.set_next(new_node)

    def remove_from_head(self):
        # what is the list is empty?
        if not self.head:
            return None
        # what if it isn't empty
        else:
            # get the value at the head
            value = self.head.get_value()
            # remove value at head
            self.head = self.head.get_next()
            # update self.head
            return value

    def count_nodes(self):
      if not self.head:
        return 0
      elif self.head.get_next() == None:
        return 1
      else:
        node_count = 0
        cur = self.head
        while cur is not None:
          cur = cur.next_node
          node_count +=1

        return node_count



    
                