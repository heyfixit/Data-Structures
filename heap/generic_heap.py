class Heap:
  def __init__(self, comparator = None):
    self.storage = []
    self.comparator = comparator
    if comparator == None:
      self.comparator = lambda a,b: a > b


  def insert(self, value):
    # add value to next available spot
    # swap up the heap until
    # the 'heap property' is valid
    # wikipedia says any value at index n might have
    # children at index 2n + 1 and 2n + 2

    self.storage.append(value)
    current_index = len(self.storage) - 1

    self._bubble_up(current_index)

  def delete(self):
    # return None if the Heap is empty
    if len(self.storage) == 0:
      return None

    deleted_item = self.storage.pop(0)

    # do nothing if that was the last item
    if len(self.storage) == 0:
      return deleted_item

    # shuffle the last item to the front
    self.storage.insert(0, self.storage.pop(-1))

    self._sift_down(0)

    return deleted_item

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = (index - 1) // 2
    current_index = index
    while parent_index >= 0:
      if self.comparator(self.storage[current_index], self.storage[parent_index]):
        self.storage[current_index], self.storage[parent_index] = self.storage[parent_index], self.storage[current_index]
      else:
        break

      current_index = parent_index
      parent_index = (current_index - 1) // 2

  def _sift_down(self, index):
    current_index = index

    while True:
      did_swap = False
      left_index = 2 * current_index + 1
      right_index = 2 * current_index + 2
      if right_index < self.get_size():
        # then we know we have 2 children
        if self.comparator(self.storage[left_index], self.storage[right_index]):
          # left child is largest value among children
          if self.comparator(self.storage[left_index], self.storage[current_index]):
            # left child was greater, swap left
            self.storage[left_index], self.storage[current_index] = self.storage[current_index], self.storage[left_index]
            current_index = left_index
            did_swap = True
        else:
          # deal with right child
          if self.comparator(self.storage[right_index], self.storage[current_index]):
            # right child was greater, swap left
            self.storage[right_index], self.storage[current_index] = self.storage[current_index], self.storage[right_index]
            current_index = right_index
            did_swap = True
      elif left_index < self.get_size():
        if self.comparator(self.storage[left_index], self.storage[current_index]):
          # left child was greater, swap left
          self.storage[left_index], self.storage[current_index] = self.storage[current_index], self.storage[left_index]
          current_index = left_index
          did_swap = True

      if not did_swap:
        break
