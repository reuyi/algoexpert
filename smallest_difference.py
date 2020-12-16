# O(nlog(n) + mlog(m)) time, O(1) space
def smallest_difference(array1, array2):
  array1.sort()
  array2.sort()
  index1 = 0
  index2 = 0
  smallest = float("inf")
  current = float("inf")
  smallest_pair = []
  while index1 < len(array1) and index2 < len(array2):
    first_num = array1[index1]
    second_num = array2[index2]
    if first_num < second_num:
      current = second_num - first_num
      index1 += 1
    elif first_num > second_num:
      current = first_num - second_num
      index2 += 1
    else:
      return [first_num, second_num]
    if smallest > current:
      smallest = current
      smallest_pair = [first_num, second_num]
  return smallest_pair
