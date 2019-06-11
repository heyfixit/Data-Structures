class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_branch = BinarySearchTree(value)
    current_branch = self

    # seek this value's spot
    # traverse the tree until we find the missing
    # branch that can hold this value
    while True:
      if current_branch.value <= value:
        if current_branch.right:
          current_branch = current_branch.right
        else:
          current_branch.right = new_branch
          break
      elif current_branch.value > value:
        if current_branch.left:
          current_branch = current_branch.left
        else:
          current_branch.left = new_branch
          break

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass