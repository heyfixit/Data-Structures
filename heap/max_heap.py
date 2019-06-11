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

    # if we're at the first index, return
    # we only have one element
    if current_index == 0:
      return

    # loop through the parents, swapping them if they're less than current child
    while True:
      parent_index = (current_index - 1) // 2

      # if the parent index is < 0, we've hit the top
      if parent_index < 0:
        break

      if self.storage[current_index] > self.storage[parent_index]:
        # swap
        self.storage[current_index], self.storage[parent_index] = self.storage[parent_index], self.storage[current_index]
      else:
        # we're in the right spot
        break

      # otherwise set the current_index to the parent_index and go again
      current_index = parent_index

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
