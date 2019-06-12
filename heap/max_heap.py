class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # add value to next available spot
    # swap up the heap until
    # the 'heap property' is valid
    # wikipedia says any value at index n might have
    # children at index 2n + 1 and 2n + 2

    self.storage.append(value)
    current_index = len(self.storage) - 1

    self._bubble_up(current_index)
    # while self._bubble_up(current_index):
      # current_index = (current_index - 1) // 2

  def delete(self):
    # print("Storage: ", self.storage)
    if len(self.storage) == 0:
      return None

    deleted_item = self.storage.pop(0)

    # do nothing if that was the last item
    if len(self.storage) == 0:
      return deleted_item

    # shuffle the last item to the front
    self.storage.insert(0, self.storage.pop(-1))

    # print("Deleted: ", deleted_item)
    # print("Sifting")
    self._sift_down(0)
    # print("Result: ", self.storage)

    return deleted_item

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = (index - 1) // 2
    if(parent_index >= 0
    and self.storage[parent_index] < self.storage[index]):
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # always swap with the smallest child
    if(right_index < self.get_size()):
      # then we have 2 children
      if self.storage[left_index] >= self.storage[right_index]:
        if self.storage[left_index] > self.storage[index]:
          self._bubble_up(left_index)
          self._sift_down(left_index)
      elif self.storage[right_index] > self.storage[left_index]:
        if self.storage[right_index] > self.storage[index]:
          self._bubble_up(right_index)
          self._sift_down(right_index)
    elif(left_index < self.get_size()):
      # we have one child
      if self.storage[left_index] > self.storage[index]:
        self._bubble_up(left_index)
        self._sift_down(left_index)

# heap = Heap()
# heap.insert(6)
# heap.insert(8)
# heap.insert(10)
# heap.insert(9)
# heap.insert(1)
# heap.insert(9)
# heap.insert(9)
# heap.insert(5)
# heap = Heap()
# heap.insert(1)
# heap.insert(10)
# heap.insert(40)
# heap.insert(2)
# heap.insert(11)
# heap.insert(11)
# print(heap.storage)
# heap.delete()
# # heap.delete()
# # heap.delete()
# print(heap.storage)
