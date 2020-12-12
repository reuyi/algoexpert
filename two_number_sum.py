# O(n) time, O(n) space
def two_number_sum(array, target_sum):
  nums = {}
  for num in array:
    potential_match = target_sum - num
    if potential_match in nums:
      return [potential_match, num]
    else:
      nums[num] = True
  return []

# O(nlog(n)) time, O(1) space
def two_number_sum(array, target_sum):
  array.sort()
  left = 0
  right = len(array) - 1
  while left < right:
    current_sum = array[left] + array[right]
    if current_sum == target_sum:
      return [array[left], array[right]]
    elif current_sum < target_sum:
      left += 1
    elif current_sum > target_sum:
      right -= 1
  return []
