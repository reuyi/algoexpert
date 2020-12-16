# O(n) time, O(1) space
def is_monotonic(array):
  if len(array) <= 2:
    return True
  direction = array[1] - array[0]
  for i in range(2, len(array)):
    if direction == 0:
      direction = array[i] - array[i-1]
      continue
    if breaks_direction(direction, array[i-1], array[i]):
      return False
  return True
 
def breaks_direction(direction, previous_int, current_int):
  difference = current_int - previous_int
  if direction > 0:
    return difference < 0:
  return difference > 0

def is_monotonic(array):
  is_non_decreasing = True
  is_non_increasing = True
  for i in range(1, len(array)):
    if array[i] < array[i-1]:
      is_non_decreasing = False
    if array[i] > array[i-1]:
      is_non_increasing = False 
  return is_non_decreasing or is_non_increasing
