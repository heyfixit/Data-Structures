"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is pointed to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      self.head = ListNode(value)
      self.tail = self.head

    self.length += 1


  def remove_from_head(self):
    if not self.head and not self.tail:
      return None

    current_head = self.head

    if self.length == 1:
      self.tail = None
      self.head = None
      self.length = 0
      return current_head.value


    self.length -= 1
    self.head = current_head.next
    self.head.prev = None

    if self.length == 1:
      self.tail = self.head

    return current_head.value

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      self.head = ListNode(value)
      self.tail = self.head

    self.length += 1

  def remove_from_tail(self):
    if not self.tail and not self.head:
      return None

    current_tail = self.tail

    if self.length == 1:
      self.head = None
      self.tail = None
      self.length = 0
      return current_tail.value


    self.length -= 1
    self.tail = current_tail.next
    self.tail.prev = None

    if self.length == 1:
      self.head = self.tail

    return current_tail.value

  def move_to_front(self, node):
    node.delete()
    self.length -= 1
    self.add_to_head(node.value)

  def move_to_end(self, node):
    if self.head == node:
      # we're at the head
      value = self.remove_from_head()
      self.add_to_tail(value)
    else:
      node.delete()
      self.length -= 1
      self.add_to_tail(node.value)

  def delete(self, node):
    if self.head == node:
      self.remove_from_head()
    elif self.tail == node:
      self.remove_from_tail()
    else:
      node.delete()

  def get_max(self):
    current_node = self.head
    if not current_node:
      return None

    max_value = current_node.value
    while current_node.next:
      current_node = current_node.next
      if current_node.value > max_value:
        max_value = current_node.value

    return max_value
