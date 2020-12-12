# O(n^2) time, O(n) space

def three_number_sum(array, target_sum):
  array.sort()
  triplets = []
  for i in range(len(array) - 2):
    left = i + 1
    right = len(array) - 1
    while left < right:
      current_sum = array[i] + array[left] + array[right]
      if current_sum == target_sum:
        triplets.append([array[i], array[left], array[right]])
        left += 1
        right -= 1
      elif current_sum < target_sum:
        left += 1
      elif current_sum > target_sum:
        right -= 1
  return triplets
