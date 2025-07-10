class Array:
  def __init__(self):
    # initialized to an empty list 
    self.data = []

  def append(self, value):
    # adds a value to the end of the list
    self.data.append(value)

  def get(self, index):
    # access via index and retrieves the value 
    if 0 <= index < len(self.data):
        return self.data[index]
    else:
        raise IndexError("index out of bounds")

  def update(self, index, value):
    # updates the value at given index with a new one 
    if 0 <= index < len(self.data):
        self.data[index] = value 
    else:
        raise IndexError("index out of bounds")

  def remove_at(self, index):
    # deletes a value at the given index
    if 0 <= index < len(self.data):
        return self.data.pop(index)
    else:
        raise IndexError("index out of bounds")

  def __len__(self):
    # return the number of items in the array 
    return len(self.data)

  def __str__(self):
    # string representation
    return str(self.data)

# --- example / testng  ---
if __name__ == "__main__":
  example = Array()
  print("example array:", example)
  
  # removing from empty list 
  # example.remove_at(2) # throws index out of bounds error 
  example.append(10)
  example.append(15)
  example.append(20)
  example.append(25)
  print("after appends:", example) # [10, 15, 20, 25]
  
  example.remove_at(1)
  print("after remove_at:", example) # [10, 15, 25]
  
  print("got the value at index 0:", example.get(0))
  print("got the value at index 1:", example.get(1))
  print("got the value at index 2:", example.get(2))
  # print(example.get(3))  # throws index out of bounds error 
  
  example.update(2, 100)
  print("after updating at index 2 with value100:", example)
